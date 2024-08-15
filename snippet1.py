# out0 = load_mean('elastic_e10')
# out0_lr4 = load_mean('lr/test_elastic_e10_lr4_n40000')
# out0_lr6 = load_mean('lr/test_elastic_e10_lr6_n40000')
# out0_lr7 = load_mean('lr/test_elastic_e10_lr7_many_n2400')
# out0_lr9 = load_mean('lr/test_elastic_e10_lr9_many_n4800')
# out0_lr15 = load_mean('lr/test_elastic_e10_lr15_many_n2400')
# labels2 = labels

out0_lr5 = load_mean('train_elastic_e10_n40000')
out0_lr4 = load_mean('lr/train_elastic_e10_lr4_n40000')
out0_lr6 = load_mean('lr/train_elastic_e10_lr6_n40000')
out0_lr7 = load_mean('lr/train_elastic_e10_lr7_many_n2400')
out0_lr9 = load_mean('lr/train_elastic_e10_lr9_many_n4800')
out0_lr15 = load_mean('lr/train_elastic_e10_lr15_many_n2400')
labels2 = train_labels

# out1 = out0_lr4[:, 0]
# out2 = out0_lr5[:, 0]
# out3 = out0_lr6[:, 0]
out1 = out0_lr4[:, 0]
out2 = out0_lr6[:, 0]
out3 = out0_lr7[:, 0]
# out1 = out0_lr6[:, 0]
# out2 = out0_lr7[:, 0]
# out3 = out0_lr9[:, 0]

m = 1000

xx = (out2 - out1)
yy = (out3 - out1)
print(scipy.stats.pearsonr(xx.tolist(), yy.tolist()))
plt.scatter(xx.tolist(), yy.tolist(), s=1)
m1, m2 = xx.min().item(), xx.max().item()
plt.plot([m1, m2], [m1, m2], color='gray', linestyle='--')
plt.plot([m1, m2], [1.5*m1, 1.5*m2], color='gray', linestyle='--')
plt.xlabel('$z_{0.5} - z_{0.4}$', fontsize=15)
plt.ylabel('$z_{0.6} - z_{0.5}$', fontsize=15)
plt.show()

