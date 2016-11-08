#!/usr/bin/env Rscript

library(ggplot2)

args <- commandArgs(trailingOnly = T)
FILE_DIR <- args[1]

plot.name = paste(strsplit(FILE_DIR, '/')[[1]][-1], collapse='/')
data.label_per_image <- read.csv(paste(FILE_DIR, '/labels_per_image.csv', sep=''))

title <- sprintf('Labels per image\n(%s)', plot.name)
plot_data <- function(filename, data, type, width = 1200, height = 600, units = "px") {
    #p <- ggplot() + geom_point(data = data, aes(x = word, y = count)) + labs(title = title, x = "# labels", y = '# images') + theme_minimal()
    #ggsave(filename, p, width = 30, height = 15, units = 'cm')
    png(filename=filename, width = width, height = height, units = units)
    plot(data, main=title, xlab='# labels', ylab='# images', type = type)
    dev.off()
}


data <- data.label_per_image

plot_data(paste(FILE_DIR, '/labels_per_image__line.png', sep=''), spline(data), type='l')
plot_data(paste(FILE_DIR, '/labels_per_image__points.png', sep=''), data, type="p")

