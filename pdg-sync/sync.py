import os
import sys
import json
import httpx
from httpx import HTTPError
import json as json_
import pathlib
from urllib.parse import quote, urlencode
import time
from slugify import slugify
import frontmatter
import sys
from os.path import exists
import requests

def load_config(path="."):
	"Load table configuration files"
	config = {"tables": []}
	for filename in os.listdir(path):
		if filename.endswith(".json"):
			try:
				with open(os.path.join(path, filename)) as config_file:
					config_data = json.load(config_file)

				config['tables'].append(config_data)
			except Exception as e:
				print(e)
				print("Could not read from {}".format(filename))
		else:
			continue
	return config

def convert_to_fieldnames(fields, col_map):
	"Return a dict using fieldnames rather than column titles"
	field_map = col_map
	# If field key is in field_map, output with field_map value as the new key
	# If field key is NOT in field_map, report error and leave out
	outfields = {}
	for k, v in fields.items():
		if field_map.get(k,False):
			if field_map[k].get('short',False):
				outfields[field_map[k]['short']] = v

	return outfields

def convert_base(
	output_path,
	base_id,
	tables,
	key,
	sqlite,
	verbose = False,
	http_read_timeout = 30.0,
	user_agent = None,
	json = True,
	ndjson = False,
	yaml = False,
	fields={}
):
	"Export Airtable data to YAML, JSON or SQLITE file on disk"
	output = pathlib.Path(output_path)
	output.mkdir(parents=True, exist_ok=True)
	if not json and not ndjson and not yaml and not sqlite:
		yaml = True
	write_batch = lambda table, batch: None
	if sqlite:
		db = sqlite_utils.Database(sqlite)
		write_batch = lambda table, batch: db[table].insert_all(
			db_batch, pk="airtable_id", replace=True, alter=True
		)
	for table_id, table in tables.items():
		records = []
		try:
			db_batch = []
			for record in all_records(
				base_id, table, key, http_read_timeout, user_agent=user_agent
			):
				r = {
					**{"airtable_id": record["id"]},
					**convert_to_fieldnames(record["fields"],fields[table_id]),
					**{"airtable_createdTime": record["createdTime"]},
				}
				records.append(r)
				db_batch.append(r)
				if len(db_batch) == 100:
					write_batch(table_id, db_batch)
					db_batch = []
		except HTTPError as exc:
			raise exc
		write_batch(table_id, db_batch)
		filenames = []
		if json:
			filename = "{}.json".format(table_id)
			dumped = json_.dumps(records, sort_keys=True, indent=4)
			(output / filename).write_text(dumped, "utf-8")
			filenames.append(output / filename)
		if ndjson:
			filename = "{}.ndjson".format(table_id)
			dumped = "\n".join(json_.dumps(r, sort_keys=True) for r in records)
			(output / filename).write_text(dumped, "utf-8")
			filenames.append(output / filename)
		if yaml:
			filename = "{}.yml".format(table_id)
			dumped = yaml_.dump(records, sort_keys=True)
			(output / filename).write_text(dumped, "utf-8")
			filenames.append(output / filename)
		if verbose:
			print(
				"Wrote {} record{} to {}".format(
					len(records),
					"" if len(records) == 1 else "s",
					", ".join(map(str, filenames)),
				)
			)


def all_records(base_id, table, api_key, http_read_timeout, sleep=0.2, user_agent=None):
	headers = {"Authorization": "Bearer {}".format(api_key)}
	if user_agent is not None:
		headers["user-agent"] = user_agent

	if http_read_timeout:
		timeout = httpx.Timeout(5, read=http_read_timeout)
		client = httpx.Client(timeout=timeout)
	else:
		client = httpx

	first = True
	offset = None
	while first or offset:
		first = False
		url = "https://api.airtable.com/v0/{}/{}?returnFieldsByFieldId=True".format(base_id, quote(table,safe='')) # ?returnFieldsByFieldId=True
		if offset:
			url += "&" + urlencode({"offset": offset})

		response = client.get(url, headers=headers)
		response.raise_for_status()
		data = response.json()
		offset = data.get("offset")
		yield from data["records"]
		if offset and sleep:
			time.sleep(sleep)

def record_map(apiID, on_field='airtable_id'):
	base_map = {'all':{}}
	for filename in os.listdir("cache/{}".format(apiID)):
		if filename.endswith(".json"):
			with open(os.path.join("cache", apiID, filename)) as table_file:
				table_map = {}
				table_data = json.load(table_file)
				for row in table_data:
					if row.get(on_field,False):
						table_map[row.get(on_field)] = row
						base_map['all'][row.get(on_field)] = row
						base_map['all'][row.get(on_field)]['table'] = filename.replace(".json","")
				base_map[filename.replace(".json","")] = table_map
	return base_map

def fetch_attachment(url, filename):
	output = pathlib.Path('../assets/pdg')
	output.mkdir(parents=True, exist_ok=True)
	path = "../assets/pdg/{}".format(filename)
	if exists(path):
		pass
	else:
		print("Downloading {}".format(filename))
		r = requests.get(url)  
		with open(path, 'wb+') as att:
			att.write(r.content)
			att.close()
	
	return path.replace("../","/")

def write_markdown(record, table, data, processed_cache):
	# Make sure path exists
	folder = '../_pdg-{}'.format(table)
	output = pathlib.Path(folder)
	output.mkdir(parents=True, exist_ok=True)

	# Create a slug
	try:
		slug = slugify(record['title'])
	except:
		try:
			slug = slugify(record['name'])
		except:
			slug = slugify(record['airtable_id'])
	
	# Open file to write
	with open('{}/{}.md'.format(folder,slug), 'w+') as f:
		post = frontmatter.loads(f.read())
		post['title'] = record.get('title','')
		post.content = record.get('description','')
		for field, value in record.items():
			# Where tags are requested, check if we've got relationships and resolve them
			if '_tag' in field:
				if isinstance(value, (list)):
					tags = []
					for tag_item in value:
						if tag_item in data['all']:
							tags.append(data['all'][tag_item].get('title',"NO TITLE"))
						else:
							tags.append(tag_item)
				else:
					tags = value
				post[field] = tags
			elif '_link' in field:
				if not isinstance(value, (list)):
					value = [value]
				links = []
				for link_item in value:
					if link_item in data['all']:
						if not link_item in processed_cache:
							processed_cache = write_markdown(data['all'][link_item], data['all'][link_item]['table'], data, processed_cache)
							processed_cache.append(link_item)

						links.append(slugify(data['all'][link_item].get('title',"No title")))
					else:
						links.append("missing-item")

				post[field] = links
			elif field in ['attachments','impact_photo','issue_photo']:
				attachment_list = []
				for attachment in value:
					attachment_list.append(fetch_attachment(attachment['thumbnails']['large']['url'], "{}-{}".format(slug,attachment['filename'])))
				post[field] = attachment_list
			else:
				post[field] = str(value).strip()
			processed_cache.append(record['airtable_id'])
		f.seek(0)
		f.write(frontmatter.dumps(post))
		f.truncate()
		f.close()
		return processed_cache

config = load_config()

processed_cache = []

for base in config['tables']:

	if len(sys.argv) > 1:
		print("Downloading {}".format(base['config']['title']))
		convert_base(base_id=base['config']['apiID'],
					 output_path="./cache/{}".format(base['config']['apiID']), 
					 key=os.environ.get("AIRTABLE_API_KEY"),
					 tables=base['tablemap'],
					 fields=base['tables'],
					 sqlite=False)  # sqlite="db/{}.db".format(base['config']['title'].replace(" ", "").replace("/", ""))
	data = record_map(base['config']['apiID'])
	
	for case_id, case in data['cases'].items():
		if case.get('status','') == 'Stage 1':
			processed_cache = write_markdown(case, 'cases', data, processed_cache)
			print(case['title'])
