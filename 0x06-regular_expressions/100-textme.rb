#!/usr/bin/env ruby
mess=""
mess+=puts ARGV[0].scan(/\[from:.*?\]/).join
mess+=(',')
mess+=puts ARGV[0].scan(/\[to:.*?\]/).join
mess+=(',')
mess+=puts ARGV[0].scan(/\[flags:.*?\]/).join
puts mess
