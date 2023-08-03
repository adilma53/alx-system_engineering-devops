#!/usr/bin/env ruby
pattern = /(?<=from|to|flags):(\+?\w+|[-?[0-1]:?]+)/

File.open('logfile.txt').each do |line|
  match_data = line.match(pattern)
  if match_data
    sender = match_data[1]
    receiver = match_data[2]
    flags = match_data[3]
    puts "#{sender},#{receiver},#{flags}"
  end
end