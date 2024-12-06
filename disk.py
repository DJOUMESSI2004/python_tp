if __name__ == '__main__':
    pass

# classe de gestion de disque de stockage 

class Disk:
    def __init__(self, total, used):
        self.total = total
        self.used = used

    @property
    def free(self):
        return self.total - self.used

    @property
    def used_perc(self):
        return self.used / self.total

    def __str__(self):
        return f"Disk[total: {self.total} Gb, used: {self.used} Gb]"

    def __lt__(self, other):
        return self.used_perc < other.used_perc

if __name__ == '__main__':
    disk1 = Disk(10, 2)
    disk2 = Disk(20, 5)
    print(disk1.free)         
    print(disk2.free)         
    print(disk1.used_perc)  
    print(disk2.used_perc)   
    disks = [disk2, disk1]
    disks_sorted = sorted(disks)
    print([str(d) for d in disks_sorted])









