import trackhub
import os

hub, genomes_file, genome, trackdb = trackhub.default_hub(
    hub_name="riboseq_hub",
    short_label="Riboseq Hub",
    long_label="RiboSeq Track Hub",
    genome="hg38",
    email="thibaut.ackaert@student.howest.be",
)

print(hub)
print(genome)

samples = [
    {"name": "sample1", "url": "https://hgdownload.soe.ucsc.edu/goldenPath/hg38/phyloP100way/hg38.phyloP100way.bw", "color": "255,128,0"},
    {"name": "sample2", "url": "https://hgdownload.soe.ucsc.edu/goldenPath/hg38/phyloP100way/hg38.phyloP100way.bw", "color": "0,128,255"},
    {"name": "sample3", "url": "https://hgdownload.soe.ucsc.edu/goldenPath/hg38/phyloP100way/hg38.phyloP100way.bw", "color": "0,200,100"},
]

for sample in samples:
    track = trackhub.Track(
        name=sample["name"],
        tracktype="bigWig",
        short_label=sample["name"],
        long_label=f"Riboseq track {sample['name']}",
        color=sample["color"],
    )
    track.add_params(bigdata_url=sample["url"])
    trackdb.add_tracks(track)

os.makedirs("stage_hub/hg38", exist_ok=True)

with open("staged_hub/hub.txt", "w") as f:
    f.write(str(hub))

with open("staged_hub/riboseq_hub.genomes.txt", "w") as f:
    f.write(str(genomes_file))

with open("staged_hub/hg38/trackDb.txt", "w") as f:
    f.write(str(trackdb))

print("Hub files written to staged_hub/")