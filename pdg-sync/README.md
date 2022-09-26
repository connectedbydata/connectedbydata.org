Participatory Data Governance Case Database - AIRTABLE -> YAML CONVERSION
=========================================================================

This directory contains *very rough and ready* code to:

* Fetch records from the Airtable API

* Turn these into Markdown + YAML Frontmatter files for Jekyll following a mapping provided in the `sync/config.json` file

* Map relationships from Airtable either into cross-reference slugs, or simple title arrays

* Fetch attachments and store them in the `assets` directory.

This is adapted from scripts originally developed for filtered AirTable -> Airtable sync for the Global Voices Civic Media Observatory. 

## Setup

```
python3 -m venv .ve
source .ve/bin/activate
pip install -r requirements.txt
````

Export your Airtable API key as an environment variable with:

```
export AIRTABLE_API_KEY=<api_key>
```

## Configuration

The `config.json` file can be generated using a script installed on the target Airtable. 

This produces a mapping file that can be used to assign shortnames to each field (used as the YAML keys when outputting markdown).

The mapping file can also be consulted to find the column heading name used in Airtable. 


## Running the scripts

```
cd sync
python sync.py Download
```

Omit the 'Downlod' keyword if you want to re-run conversation from cached data, rather than fetching updated data.

### Caveats

The scripts do not perform any cleanup or deletion, so you may wish to remove all `_pdg-` folders prior to a sync to have a clean copy of the data. 


## Airtable Script

```javascript

function build_map(debug=false) {
    let map = {"config":{},"tables":{},"tablemap":{}}
    map['config']['title'] = base.name;
    map['config']['apiID'] = base.id;

    let tables = base.tables
    for (let table of tables) {
        try {
            tableshort = table.id
            
            map['tablemap'][tableshort] = table.name
            table_map = {}
            for (let field of table.fields) {
                try {
                    shortname = field.id
                    if(!(shortname)) { throw new Error("") }
                    table_map[shortname] = {'short':'', 'long':field.name }
                } catch {
                    if(debug) {
                        output.inspect(table.name + " is missing short name for: " + field.name + ".\n\n Please add a [SHORTNAME] to the start of the column description.")
                    }
                }
                
            }
            map['tables'][tableshort] = table_map
        } catch {
            if(debug) {
                output.inspect(table.name + " is missing short name. Please add a [SHORTNAME] to the start of the table description.")
            }
        }
    }
    return map;
}

let displayOrModify = await input.buttonsAsync('Display table info?', ['Display']);

if (displayOrModify == 'Display') {
    output.text(JSON.stringify(build_map(debug=true)))
} else {
   output.text("Ok. We won't do anything right now.")
}
```