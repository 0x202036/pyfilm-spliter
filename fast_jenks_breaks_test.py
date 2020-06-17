import jenkspy
from analyser.caption_factory import CaptionFactory


def cut(li, low, high):
    new_list = []
    for i in li:
        if low < i <= high:
            new_list.append(i)
    return len(new_list)


s_list = CaptionFactory.load_dir(r"H:\开发\样本\film spliter\字幕原文件", 0, "")
num_list = [len(s.s_en) for s in s_list]
breaks = jenkspy.jenks_breaks(num_list, 3)
print("min="+str(min(num_list))+",max="+str(max(num_list))+",breaks="+str(breaks))
print("11<x<=45:%s\n45<x<=94:%s\n94<x<=296:%s\n" % (cut(num_list, 11, 45), cut(num_list, 45, 94), cut(num_list, 94, 296)))
for s in s_list:
    if len(s.s_en) == breaks[3]:
        print(s.s_en+"\n"+s.s_cn)
        break


