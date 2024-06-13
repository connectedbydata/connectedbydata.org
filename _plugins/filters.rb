module Jekyll
module Filters
module CustomFilters

MARKDOWN_INLINERS = { # Must be uninterpretable by Markdown!
	open: '{inline}',
	close: '{/inline}'
}.freeze
private_constant(:MARKDOWN_INLINERS)

# Convert markdown to HTML inline elements, don't wrap it in <p> tags
def markdownify_inline(input)

	block = input.dup.to_s.strip

	if block.length > 0
		block = inlinify(block)

		# If this is a heading, reduce to a para
		block = block.gsub(/^\#+\s*/, '')

		# Add delimiters to force any other string into a paragraph
		block = MARKDOWN_INLINERS[:open] + inlinify(block) + MARKDOWN_INLINERS[:close]

		# Covnert Markdown to HTML
		block = @context.registers[:site].find_converter_instance(
			Jekyll::Converters::Markdown
		).convert(block) # Should see input as 1 paragraph
		block = inlinify(block) # Inlinify again just in case

		# Remove the <p> tags that Markdown conversion will add, to get an HTML fragment
		block = block.gsub(
			Regexp.new(
				'(^(<p>)?\s*' +
				Regexp.escape(MARKDOWN_INLINERS[:open]) + '|' +
				Regexp.escape(MARKDOWN_INLINERS[:close]) +
				'\s*(<\/p>)?$)'
			),
		'')
	end

	return block

end

# Remove all newlines from the content
def inlinify(content)
	content = content.to_s
	content = split_newlines(content)
	content = content.each{ |s| s.strip }.join(' ')
	content
end

# Split content into an array at newlines
def split_newlines(content)
	if content.length > 0
		content = [content] if !content.is_a?(Array)
		content.flatten!
		content.map! { |part|
			part.to_s.split(/[\n\r]+/)
		}
		content.flatten!
		content.reject!(&:empty?)
		return content
	else
		return []
	end
end

# Get key(s) or value(s) of a hash as an array
def keys(hash)
	hash_extract(hash, :keys)
end
def key(hash) keys(hash).first end
def values(hash)
	hash_extract(hash, :values)
end
def value(hash) values(hash).first end

private

def hash_extract(hash, aspect)
	if hash.is_a?(Hash)
		case aspect
		when :keys
			return hash.keys
		when :values
			return hash.values
		end
	elsif hash.is_a?(Array)
		case aspect
		when :keys
			return hash.each_index.to_a
		when :values
			return hash
		end
	else
		return [hash]
	end
end

end
end
end

Liquid::Template.register_filter(Jekyll::Filters::CustomFilters)