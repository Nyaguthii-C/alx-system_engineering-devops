#!/usr/bin/env ruby
mess=""
mess+=ARGV[0].scan(/\[from:(.*?)\]/).join
mess+=(',')
mess+=ARGV[0].scan(/\[to:(.*?)\]/).join
mess+=(',')
mess+=ARGV[0].scan(/\[flags:(.*?)\]/).join
puts mess
