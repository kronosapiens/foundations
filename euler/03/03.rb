# https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

require 'prime'
require 'benchmark'

class LPF

  def self.find_lpf(prime)

    primes = Prime.each

    factor_array = []
    prime_fac = primes.next

    while prime_fac <= prime
      if (prime % prime_fac) == 0
        factor_array << prime_fac
        prime = prime / prime_fac
      else
        prime_fac = primes.next
      end
    end

    factor_array

  end

end

puts Benchmark.measure { puts LPF.find_lpf(600851475143) }

# [1] pry(main)> load '03.rb'
# 71
# 839
# 1471
# 6857
#   0.000000   0.000000   0.000000 (  0.003170)
# => true


