input = gets.split(' ').map(&:to_i)

range = (input[0] - input[1]).abs / 2
exp = ((input[0]+1) / 2) + ((input[1]+1) / 2) 

offset = 0
if(input[0].even? and input[1].even?) then
	offset = 1
end

(exp-range+offset...exp+range+offset+1).each do |n|
	puts n
end