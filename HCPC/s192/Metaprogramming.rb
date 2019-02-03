def eval(map, a, op, b)
	if map[a] == nil or map[b] == nil
		puts 'undefined'
	elsif op.eql?('<')
		puts map[a].to_i < map[b].to_i
	elsif op.eql?('>')
		puts map[a].to_i > map[b].to_i
	else
		puts map[a].to_i == map[b].to_i
	end
end
	
vars = Hash.new
STDIN.each_line do |line|
	line = line.chomp
	if line.eql?('')
		break
	end
	line = line.split(' ')
	if line[0].eql?('define')
		vars.store(line[2], line[1].to_i)
	elsif line[0].eql?('eval')
		eval(vars, line[1], line[2], line[3])
	else
		puts 'help'
	end
end