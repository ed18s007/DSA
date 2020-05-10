def tower_of_hanoi_soln(num_disks, source, auxilary, destination):
	if num_disks==0:
		return 
	if num_disks==1:
		print("{} {}".format(source, destination))
		return
	tower_of_hanoi_soln(num_disks-1, source, destination, auxilary)
	print("here",num_disks)
	print("{} {}".format(source, destination))
	tower_of_hanoi_soln(num_disks-1, auxilary, source, destination)

def tower_of_hanoi(num_disks):
	return tower_of_hanoi_soln(num_disks, 'S','A','D')

tower_of_hanoi(2)