# components_database.py

# Dictionary to store computer components and their options
components_database = {
    "CPU": ["INTEL Core i3", "AMD Ryzen 3", "INTEL Core i5", "AMD Ryzen 5", "INTEL Core i7", "AMD Ryzen 7", "INTEL Core i9", "AMD Ryzen 9"],
    "GPU": ["NVIDIA GTX 1650", "AMD RX 5500 XT", "NVIDIA GTX 1660 Super", "AMD RX 5600 XT", "NVIDIA RTX 3060", "AMD RX 6700 XT", "NVIDIA RTX 3080", "AMD RX 6800 XT", "NVIDIA RTX 4090"],
    "RAM": ["8GB DDR4 Corsair Vengeance LPX", "16GB DDR4 G.SKILL Ripjaws V", "32GB DDR4 Crucial Ballistix"],
    "Storage": ["240GB SSD", "500GB SSD", "1TB HDD", "1TB SSD", "2TB HDD", "1TB NVMe SSD", "2TB NVMe SSD"],
    "cpucooler": ["Cooler Master Hyper 212", "Noctua NH-U12S", "Corsair H60", "NZXT Kraken X53"],
    "case": ["NZXT H510", "Fractal Design Meshify C", "Phanteks P400A", "Lian Li Lancool II", "Corsair 4000D"],
    "powersupply": ["EVGA 500 W1", "Corsair CX650M", "Seasonic Focus GX-650"],
    "motherboard": ["MSI Z490-A PRO", "MSI MPG Z590 GAMING PLUS", "MSI B550 GAMING GEN3", "MSI MAG B550 Tomahawk"]

}

# Dictionary to store computer component specifications
component_specs = {
    "INTEL Core i3": {"socket": "LGA1200", "wattage": 65},
    "AMD Ryzen 3": {"socket": "AM4", "wattage": 65},
    "INTEL Core i5": {"socket": "LGA1200", "wattage": 95},
    "AMD Ryzen 5": {"socket": "AM4", "wattage": 95},
    "INTEL Core i7": {"socket": "LGA1200", "wattage": 125},
    "AMD Ryzen 7": {"socket": "AM4", "wattage": 105},
    "INTEL Core i9": {"socket": "LGA1200", "wattage": 125},
    "AMD Ryzen 9": {"socket": "AM4", "wattage": 140},
    
    "NVIDIA GTX 1650": {"series": "GTX 16", "wattage": 75},
    "AMD RX 5500 XT": {"series": "RX 5000", "wattage": 110},
    "NVIDIA GTX 1660 Super": {"series": "GTX 16", "wattage": 125},
    "AMD RX 5600 XT": {"series": "RX 5000", "wattage": 150},
    "NVIDIA RTX 3060": {"series": "RTX 30", "wattage": 170},
    "AMD RX 6700 XT": {"series": "RX 6000", "wattage": 230},
    "NVIDIA RTX 3080": {"series": "RTX 30", "wattage": 320},
    "AMD RX 6800 XT": {"series": "RX 6000", "wattage": 300},
    "NVIDIA RTX 4090": {"series": "RTX 40", "wattage": 450},
    
    "8GB DDR4 Corsair Vengeance LPX": {"type": "DDR4", "capacity": 8},
    "16GB DDR4 G.SKILL Ripjaws V": {"type": "DDR4", "capacity": 16},
    "32GB DDR4 Crucial Ballistix": {"type": "DDR4", "capacity": 32},
    
    "240GB SSD": {"type": "SSD", "capacity": 240},
    "500GB SSD": {"type": "SSD", "capacity": 500},
    "1TB HDD": {"type": "HDD", "capacity": 1000},
    "1TB SSD": {"type": "SSD", "capacity": 1000},
    "2TB HDD": {"type": "HDD", "capacity": 2000},
    "1TB NVMe SSD": {"type": "NVMe SSD", "capacity": 1000},
    "2TB NVMe SSD": {"type": "NVMe SSD", "capacity": 2000},
    
    "Cooler Master Hyper 212": {"socket": ["LGA1200", "AM4"], "compatibility": "CPU Cooler"},
    "Noctua NH-U12S": {"socket": ["LGA1200", "AM4"], "compatibility": "CPU Cooler"},
    "Corsair H60": {"socket": ["LGA1200", "AM4"], "compatibility": "AIO Liquid Cooler"},
    "NZXT Kraken X53": {"socket": ["LGA1200", "AM4"], "compatibility": "AIO Liquid Cooler"},
    
    "NZXT H510": {"size": "Mid Tower", "compatibility": "ATX, MicroATX, Mini-ITX"},
    "Fractal Design Meshify C": {"size": "Mid Tower", "compatibility": "ATX, MicroATX, Mini-ITX"},
    "Phanteks P400A": {"size": "Mid Tower", "compatibility": "ATX, MicroATX, Mini-ITX"},
    "Lian Li Lancool II": {"size": "Mid Tower", "compatibility": "ATX, E-ATX, MicroATX, Mini-ITX"},
    "Corsair 4000D": {"size": "Mid Tower", "compatibility": "ATX, MicroATX, Mini-ITX"},
    
    "EVGA 500 W1": {"wattage": 500, "modularity": "Semi-Modular"},
    "Corsair CX650M": {"wattage": 650, "modularity": "Semi-Modular"},
    "Seasonic Focus GX-650": {"wattage": 650, "modularity": "Fully Modular"},
    
    "MSI Z490-A PRO": {"socket": "LGA1200", "form_factor": "ATX"},
    "MSI MPG Z590 GAMING PLUS": {"socket": "LGA1200", "form_factor": "ATX"},
    "MSI B550 GAMING GEN3": {"socket": "AM4", "form_factor": "ATX"},
    "MSI MAG B550 Tomahawk": {"socket": "AM4", "form_factor": "ATX"},
}
