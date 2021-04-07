import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import category_encoders as ce
datawine = pd.read_csv('D:/1007storage/visual_studio/Python/data/winemag-data-130k-v2.csv/winemag.csv') #读取数据 
datavideo1 = pd.read_csv('D:/1007storage/visual_studio/Python/data/GBvideos.csv/GBvideos.csv') #读取数据
datavideo = datavideo1.head(1000)
winepoints = datawine['points']	        #读取winepoints
wineprice = datawine['price']	        #读取wineprice
wineprice1 = wineprice.dropna(axis = 0) #删除包括nan值的行
def num_nan(nums):
    print("________")
    x2 = nums.isnull().sum().sum()    #读取nums中的nan值
    return x2
def fiveNumber(nums):#五数概括 Minimum（最小值）、Q1、Med-ian（中位数、）、Q3、Maximum（最大值）
	Minimum=min(nums)
	Maximum=max(nums)
	Q1=np.percentile(nums,25)
	Median=np.median(nums)
	Q3=np.percentile(nums,75)
	IQR=Q3-Q1
	lower_limit=Q1-1.5*IQR #下限值
	upper_limit=Q3+1.5*IQR #上限值
	print("Minimum,Q1,Median,Q3,Maximum")
	return Minimum,Q1,Median,Q3,Maximum
#绘制直方图————————————————————————————————————
def histpic(nums1,nums2,nums3,nums4,d,histname):               #绘制直方图
    fig,axes = plt.subplots(nrows=2,ncols=2)
    plt.suptitle(histname,color = 'red')
    axes[0,0].set(title='delete rows with nan')
    axes[0,1].set(title='fill nan with modal number')
    axes[1,0].set(title='fill nan with behind')
    axes[1,1].set(title='fill nan with method of interpolation')
    numbins1 = int((max(nums1)-min(nums1))/d)
    numbins2 = int((max(nums2)-min(nums2))/d)
    numbins3 = int((max(nums3)-min(nums3))/d)
    numbins4 = int((max(nums4)-min(nums4))/d)
    axes[0,0].hist(nums1,numbins1)				#绘制直方图
    axes[0,1].hist(nums2,numbins2)
    axes[1,0].hist(nums3,numbins3)
    axes[1,1].hist(nums4,numbins4)
    axes[0,0].grid()                            #网格
    axes[0,1].grid()
    axes[1,0].grid()
    axes[1,1].grid()
    plt.show()
    return 1
d = 1										#组距
num_bins = int((max(winepoints)-min(winepoints))/d)
print(max(winepoints), min(winepoints), max(winepoints) - min(winepoints))
print("num_bins=",num_bins)
plt.figure(figsize=(15,10),dpi=80)	#设置图形大小
plt.suptitle("points_hist",color = 'red')
plt.hist(winepoints,num_bins)				#绘制直方图
plt.xticks(range(int(min(winepoints)),int(max(winepoints))+d,d))	#设置x轴刻度
plt.grid()
plt.show()
d = 8										#组距
num_bins = int((max(wineprice1)-min(wineprice1))/d)
print(max(wineprice1), min(wineprice1), max(wineprice1) - min(wineprice1))
print("num_bins=",num_bins)
plt.figure(figsize=(15,10),dpi=80)	#设置图形大小
plt.suptitle("price_hist",color = 'red')
plt.hist(wineprice1,num_bins)				#绘制直方图
plt.xticks(range(int(min(wineprice1)),int(max(wineprice1))+d,d))	#设置x轴刻度
plt.grid()
plt.show()
#五数概括————————————————————————————————————————
ave_points = winepoints.mean()
count_points = np.argmax(np.bincount(winepoints))
ave_price = wineprice.mean()
count_price = np.argmax(np.bincount(wineprice1))
print("__________________________")
print("__________________________")
print("points的五数概括")
print(fiveNumber(winepoints))
print("__________________________")
print("points的均值")
print('%.2f'%ave_points)
print("points的众数")
print('%.2f'%count_points)
print("__________________________")
print("__________________________")
print("price的均值（去除nan之后）")
print('%.2f'%ave_price,"、",'%.2f'%count_price)
print("price的众数（去除nan之后）")
print('%.2f'%count_price)
#因为使用plt.show之后，程序会阻塞，请手动关闭图片以继续运行
#绘制盒图————————————————————————————————————————————
plt.boxplot(x = winepoints, # 指定绘图数据
            patch_artist=True, # 要求用自定义颜色填充盒形图，默认白色填充
            showmeans=True, # 以点的形式显示均值
            boxprops = {'color':'black','facecolor':'#9999ff'}, # 设置箱体属性，填充色和边框色
            flierprops = {'marker':'o','markerfacecolor':'red','color':'black'}, # 设置异常值属性，点的形状、填充色和边框色
            meanprops = {'marker':'D','markerfacecolor':'indianred'}, # 设置均值点的属性，点的形状、填充色
            medianprops = {'linestyle':'--','color':'orange'}) # 设置中位数线的属性，线的类型和颜色
plt.suptitle("points_box_fig",color = 'red')
plt.ylim(75,105)# 设置y轴的范围
plt.tick_params(top='off', right='off')# 去除箱线图的上边框与右边框的刻度标签
plt.show()# 显示图形
plt.boxplot(x = wineprice1, # 指定绘图数据
            patch_artist=True, # 要求用自定义颜色填充盒形图，默认白色填充
            showmeans=True, # 以点的形式显示均值
            boxprops = {'color':'black','facecolor':'#9999ff'}, # 设置箱体属性，填充色和边框色
            flierprops = {'marker':'o','markerfacecolor':'red','color':'black'}, # 设置异常值属性，点的形状、填充色和边框色
            meanprops = {'marker':'D','markerfacecolor':'indianred'}, # 设置均值点的属性，点的形状、填充色
            medianprops = {'linestyle':'--','color':'orange'}) # 设置中位数线的属性，线的类型和颜色
plt.suptitle("price_box_fig",color = 'red')
plt.ylim(0,3400)# 设置y轴的范围
plt.tick_params(top='off', right='off')# 去除箱线图的上边框与右边框的刻度标签
plt.show()# 显示图形
def boxplot(nums1,nums2,nums3,nums4,dataname):                   #绘制四个盒图
    fig,axes = plt.subplots(nrows=2,ncols=2)
    plt.suptitle(dataname,color = 'red')
    axes[0,0].set(title='delete rows with nan')
    axes[0,1].set(title='fill nan with modal number')
    axes[1,0].set(title='fill nan with behind')
    axes[1,1].set(title='fill nan with method of interpolation')
    axes[0,0].boxplot(x = nums1, # 指定绘图数据
            patch_artist=True, # 要求用自定义颜色填充盒形图，默认白色填充
            showmeans=True, # 以点的形式显示均值
            boxprops = {'color':'black','facecolor':'#9999ff'}, # 设置箱体属性，填充色和边框色
            flierprops = {'marker':'o','markerfacecolor':'red','color':'black'}, # 设置异常值属性，点的形状、填充色和边框色
            meanprops = {'marker':'D','markerfacecolor':'indianred'}, # 设置均值点的属性，点的形状、填充色
            medianprops = {'linestyle':'--','color':'orange'}) # 设置中位数线的属性，线的类型和颜色
    axes[0,1].boxplot(x = nums2, # 指定绘图数据
            patch_artist=True, # 要求用自定义颜色填充盒形图，默认白色填充
            showmeans=True, # 以点的形式显示均值
            boxprops = {'color':'black','facecolor':'#9999ff'}, # 设置箱体属性，填充色和边框色
            flierprops = {'marker':'o','markerfacecolor':'red','color':'black'}, # 设置异常值属性，点的形状、填充色和边框色
            meanprops = {'marker':'D','markerfacecolor':'indianred'}, # 设置均值点的属性，点的形状、填充色
            medianprops = {'linestyle':'--','color':'orange'}) # 设置中位数线的属性，线的类型和颜色
    axes[1,0].boxplot(x = nums3, # 指定绘图数据
            patch_artist=True, # 要求用自定义颜色填充盒形图，默认白色填充
            showmeans=True, # 以点的形式显示均值
            boxprops = {'color':'black','facecolor':'#9999ff'}, # 设置箱体属性，填充色和边框色
            flierprops = {'marker':'o','markerfacecolor':'red','color':'black'}, # 设置异常值属性，点的形状、填充色和边框色
            meanprops = {'marker':'D','markerfacecolor':'indianred'}, # 设置均值点的属性，点的形状、填充色
            medianprops = {'linestyle':'--','color':'orange'}) # 设置中位数线的属性，线的类型和颜色
    axes[1,1].boxplot(x = nums4, # 指定绘图数据
            patch_artist=True, # 要求用自定义颜色填充盒形图，默认白色填充
            showmeans=True, # 以点的形式显示均值
            boxprops = {'color':'black','facecolor':'#9999ff'}, # 设置箱体属性，填充色和边框色
            flierprops = {'marker':'o','markerfacecolor':'red','color':'black'}, # 设置异常值属性，点的形状、填充色和边框色
            meanprops = {'marker':'D','markerfacecolor':'indianred'}, # 设置均值点的属性，点的形状、填充色
            medianprops = {'linestyle':'--','color':'orange'}) # 设置中位数线的属性，线的类型和颜色
    axes[0,0].tick_params(top='off', right='off')
    axes[0,1].tick_params(top='off', right='off')
    axes[1,0].tick_params(top='off', right='off')
    axes[1,1].tick_params(top='off', right='off')
    plt.show()# 显示图形
    return 1
print("填充前的wine_priced的缺失值的数量")
print(num_nan(datawine.price))
print("填充后的wine_priced的缺失值的数量")
print(num_nan(wineprice1))
print("将price中含有nan值的行删去后可得price的五数概括")
print(fiveNumber(wineprice1))#wineprice1    删去nan
print("__________________________")
wineprice2 = wineprice.fillna(count_price)#winepirce2   用众数填充nan
print("将price中用最高频率值填充nan，五数概括")
print(fiveNumber(wineprice2))
print("__________________________")
wineprice3 = wineprice.fillna(method='bfill')#数据属性的相关关系 用下一个值进行填充
print("用后一个数据填充price中的nan，五数概括")
print(fiveNumber(wineprice3))
print("__________________________")
wineprice4 =  wineprice.interpolate()#使用插值法实现对象相似性填充
wineprice4 = wineprice4.fillna(method='bfill')
print(histpic(wineprice1,wineprice2,wineprice3,wineprice4,8,"data_wine_hist"))
print(boxplot(wineprice1,wineprice2,wineprice3,wineprice4,"data_wine_boxplot"))
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

dislikes1 = datavideo['dislikes'].dropna(axis = 0)

ave_dislikes = dislikes1.mean()
count_dislikes = np.argmax(np.bincount(dislikes1))
print("dislikes的均值")
print('%.2f'%ave_dislikes)
print("dislikes的众数")
print('%.2f'%count_dislikes)
print("填充前的data_video_dislikes的缺失值的数量")
print(num_nan(datavideo.dislikes))
print("填充后的data_video_dislikes的缺失值的数量")
print(num_nan(dislikes1))
print("将dislikes中含有nan值的行删去后可得dislikes的五数概括")
print(fiveNumber(dislikes1))#wineprice1    删去nan
print("__________________________")
dislikes2 = datavideo['dislikes'].fillna(count_price)#winepirce2   用众数填充nan
print("将dislikes中用最高频率值填充dislikes，五数概括")
print(fiveNumber(dislikes2))
print("__________________________")
dislikes3 = datavideo['dislikes'].fillna(method='bfill')#数据属性的相关关系 用下一个值进行填充
print("用后一个数据填充dislikes中的nan，五数概括")
print(fiveNumber(dislikes3))
print("__________________________")
dislikes4 =  datavideo['dislikes'].interpolate()#使用插值法实现对象相似性填充
print("用插值法填充dislikes中的nan，五数概括")
#dislikes4 = dislikes4.fillna(method='bfill')
print(fiveNumber(dislikes4))
print(histpic(dislikes1,dislikes2,dislikes3,dislikes4,1000,"data_video_dislikes"))
print(boxplot(dislikes1,dislikes2,dislikes3,dislikes4,"data_video_dislikes"))