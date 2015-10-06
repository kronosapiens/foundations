# https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

require 'benchmark'

class SumMultiples

  def self.find_multiples_below(num)
    multiples_array = []
    i = 1
    while i < 1000 do
      if i % 3 == 0 || i % 5 == 0
        multiples_array << i
      end
      i += 1
    end
    multiples_array.inject(0) {|product, num| product += num}
  end

end

puts Benchmark.measure {puts SumMultiples.find_multiples_below(1000)}

# [1] pry(main)> load '01.rb'
# 233168
#   0.000000   0.000000   0.000000 (  0.000328)
# => true
