#!/usr/bin/env ruby

items = ARGV[0].scan(/\[(from|to|flags):\s*([^\]]+)\]/)

result = items.map { |item| item[1] }.join(",")

puts result
