library(ggplot2)
a2 <- read.csv("/Users/Coyawa/Git/02-DataVis-10ways/r-ggplot2/cars-sample.csv")
f <- ggplot(a2, aes(x=Weight, y=MPG, size=Weight))
g <- qplot(Weight, MPG, color = Manufacturer, size = Weight, alpha = I(0.5), data = a2)
g + theme_set(theme_bw())
g + scale_color_manual(values = c("tomato","goldenrod", "lightseagreen", "lightskyblue", "blueviolet"))


