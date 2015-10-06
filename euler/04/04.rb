# https://projecteuler.net/problem=4

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

require 'benchmark'

class Palindromic

  def self.find_palindrome(num_digits)
    right = ("9" * num_digits).to_i
    left = ("9" * num_digits).to_i

    palindrome_array = []

    while left > 0
      number = right * left
      num_string = number.to_s.chars

      match_array = []

      num_string.each_with_index { |num, i| match_array << (num == num_string[-i -1]) }
      if match_array.all?
        palindrome_array << number
      end

      right -= 1
      if right == left / 2
        right = left
        left -= 1
      end

    end

    puts palindrome_array.max
  end

end

puts Benchmark.measure { puts Palindromic.find_palindrome(1) }
puts Benchmark.measure { puts Palindromic.find_palindrome(2) }
puts Benchmark.measure { puts Palindromic.find_palindrome(3) }

# [1] pry(main)> load '04.rb'
# 9

#   0.000000   0.000000   0.000000 (  0.000152)
# 9009

#   0.030000   0.000000   0.030000 (  0.025688)
# 906609

#   1.760000   0.010000   1.770000 (  1.868538)
# => true


