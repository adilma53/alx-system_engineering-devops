#!/usr/bin/env ruby

# Regular expression pattern to extract the required information
pattern = /(?<=from|to|flags):(\+?\w+|[-?[0-1]:?]+)/

puts ARGV[0].scan(pattern).join(',')