import os

samples = [
    {"name": "sample1", "url": "https://hgdownload.soe.ucsc.edu/goldenPath/hg38/phyloP100way/hg38.phyloP100way.bw", "color": "255,128,0"},
    {"name": "sample2", "url": "https://hgdownload.soe.ucsc.edu/goldenPath/hg38/phyloP100way/hg38.phyloP100way.bw", "color": "0,128,255"},
    {"name": "sample3", "url": "https://hgdownload.soe.ucsc.edu/goldenPath/hg38/phyloP100way/hg38.phyloP100way.bw", "color": "0,200,100"},
]

os.makedirs("staged_hub/hg38", exist_ok=True)

# Write hub.txt
with open("staged_hub/hub.txt", "w") as f:
    f.write("hub riboseq_hub\n")
    f.write("shortLabel RiboSeq Hub\n")
    f.write("longLabel RiboSeq Track Hub\n")
    f.write("genomesFile genomes.txt\n")
    f.write("email thibaut.ackaert@student.howest.be\n")

# Write genomes.txt
with open("staged_hub/genomes.txt", "w") as f:
    f.write("genome hg38\n")
    f.write("trackDb hg38/trackDb.txt\n")

# Write trackDb.txt from samples list
with open("staged_hub/hg38/trackDb.txt", "w") as f:
    for sample in samples:
        f.write(f"track {sample['name']}\n")
        f.write(f"bigDataUrl {sample['url']}\n")
        f.write(f"shortLabel {sample['name']}\n")
        f.write(f"longLabel RiboSeq track {sample['name']}\n")
        f.write(f"type bigWig\n")
        f.write(f"color {sample['color']}\n")
        f.write("\n")

print("Hub generated successfully")