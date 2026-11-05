# Company info
COMPANIES = {
    "SAMSUNG": {
        "id": "3W9TOv2F3eX3x5W1zpBxiVzfti797csk9bzu62W0M2A=",
        "aliases": ["Samsung Semiconductor", "Samsung Austin Semiconductor"],
        "domain": ["https://semiconductor.samsung.com/about-us/global-network/us/", "https://semiconductor.samsung.com"]
    },
    "SK_HYNIX": {
        "id": "7tNu0DvjEyjlA2GfrfXdXj/Ow0ijDZb1dcIs85+CxdAJH3oeBDmzF3p0X4lV8vAl",
        "aliases": ["SK hynix", "SK hynix America", "SK hynix memory solutions America Inc."],
        "domain": ["skhms.com"]
    },
    "MICRON": {
        "id": "6/OIAZH/Y9hxbL0DIkTZFwwk5GSQkTIWpNfH0xlhfgs=",
        "aliases": ["Micron", "Micron Technology"],
        "domain": ["https://www.micron.com/"]
    }
}

# Filters for API call to get HBM
CORE_FILTERS = ["HBM", "high bandwidth memory"]
MEMORY_POOL_FILTERS = ["DRAM", "memory"]

# Filter mode for API call in 01_collect.py
MODES = {
    "all":    {},                                     
    "core":   {"job_description_contains_or": CORE_FILTERS},   
    "misses": {"job_description_contains_or": MEMORY_POOL_FILTERS,
               "job_description_contains_not": CORE_FILTERS},  
} 