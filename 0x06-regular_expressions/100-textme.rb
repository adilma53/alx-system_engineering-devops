#!/usr/bin/env ruby

# Regular expression pattern to extract the required information
puts ARGV[0].scan(/(?<=from|to|flags):(\+?\w+|[-?[0-1]:?]+)/).join(',')