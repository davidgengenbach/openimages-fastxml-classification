#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = T)
file_dir <- args[1]

data <- read.csv(paste(file_dir, 'labels_3_wc.txt', sep='/'))$count
print(sum(data[1:50]))
print(sum(data))
print(sum(data[1:50]) / sum(data) * 100)

plot.name = paste(strsplit(file_dir, '/')[[1]][-1], collapse='/')
plot_data <- function(filename, data, title, width = 1200, height = 600, units = "px") {
    png(filename=filename, width = width, height = height, units = units)
    #, ann=FALSE
    plot(data, main=title, xlab='labels', ylab='# images', xaxt='n')
    dev.off()
}

plot_data(paste(file_dir, 'label_distribution_99th.png', sep='/'), data[data > quantile(data, 0.99)], title=sprintf('Label distribution\n99th percentile\n(%s)', plot.name))
plot_data(paste(file_dir, 'label_distribution_25th.png', sep='/'), data[data < quantile(data, 0.25)], title=sprintf('Label distribution\n25th percentile\n(%s)', plot.name))
