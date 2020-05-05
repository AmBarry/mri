library(tidyverse)


umap <- read_csv("umap_embeddings.csv", col_names = c("UMAP1", "UMAP2"))


labels <- read_csv("umap_labels.txt")

theme_set(theme_bw())
ggplot(umap) + geom_point(aes(x=UMAP1, y=UMAP2)) + ggtitle("UMAP on 1052 brains") + theme(panel.grid = element_blank())
ggsave("brains_map.pdf")
ggsave("brains_map.png")
