#!/usr/bin/env ruby
x = ARGV[0].scan(/(\[from:(\S+)\]|\[to:(\S+)\]|\[flags:(\S+)\])/)
y = x[0][1] + "," + x[1][2] + "," + x[2][3]
puts y

