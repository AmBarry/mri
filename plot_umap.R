library(tidyverse)
library(viridis)

umap <- read_csv("umap_embedding.csv", col_names = c("UMAP1", "UMAP2"))

labels <- read_csv("umap_labels.txt", col_names = "surferID") %>%
  mutate(SUB_ID = as.integer(str_extract(surferID, pattern = "\\d+")))
umap <- umap %>% add_column(SUB_ID = labels$SUB_ID)

metadata <- read_csv("ABIDE_Phenotype.csv", na = c("", "NA", -9999))

d <- inner_join(metadata, umap, by = "SUB_ID")
d$SEX <- as.factor(d$SEX)

theme_set(theme_bw())
ggplot(d) + geom_point(aes(x=UMAP1, y=UMAP2, color = SEX)) +
  ggtitle("UMAP on 1052 brains") +
  theme(panel.grid = element_blank())
ggsave("brains_map.pdf")
ggsave("brains_map.png")

ggplot(d) +
  geom_text(aes(x=UMAP1, y=UMAP2, label =  SUB_ID), size = 1, check_overlap = T) +
  ggtitle("UMAP on 1052 brains") +
  theme(panel.grid = element_blank())
ggsave("brains_map_byid.pdf")
