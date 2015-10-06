# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

require 'benchmark'

class SmallestDivisible

  def self.find_smallest_divisible_by(max)
    found = false
    num = max
    while !found do
      if self.divisible_by(max, num)
        found = true
      else
        num += max
      end
    end
    num
  end

  def self.divisible_by(max, num_to_check)
    num_range = 1..max
    num_range.size == num_range.select {|num| num_to_check % num == 0}.size
  end

end

puts Benchmark.measure { puts SmallestDivisible.find_smallest_divisible_by(10) }
puts Benchmark.measure { puts SmallestDivisible.find_smallest_divisible_by(20) }

# [1] pry(main)> load '05.rb'
# 2520
#   0.000000   0.000000   0.000000 (  0.001137)
# 232792560
#  60.340000   0.860000  61.200000 ( 71.640382)
# => true
