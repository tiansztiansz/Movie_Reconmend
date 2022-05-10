
# 1、导入数据
## 导入 电影.xlsx 和 评分.xlsx
def reconmend(name):
  import pandas as pd
  import numpy as np

  movies = pd.read_excel('电影.xlsx')
  score = pd.read_excel('评分.xlsx')

  ## 电影.xlsx 和 评分.xlsx 合并、查看新表、导出新表、统计评分次数
  df = pd.merge(movies, score, on='电影编号')


  # 2、数据分析
  ratings = pd.DataFrame(df.groupby('名称')['评分'].mean())
  ratings.sort_values('评分', ascending=False)
  ratings['评分次数'] = df.groupby('名称')['评分'].count()
  ratings.sort_values('评分次数', ascending=False)


  # 3、数据处理
  user_movie = df.pivot_table(index='用户编号', columns='名称', values='评分')
  user_movie.tail()
  user_movie.describe()

  # 4、智能推荐
  FG = user_movie[name]
  pd.DataFrame(FG)
  corr_FG = user_movie.corrwith(FG)
  similarity = pd.DataFrame(corr_FG, columns=['相关系数'])
  similarity.dropna(inplace=True)
  similarity_new = pd.merge(similarity, ratings['评分次数'], left_index=True, right_index=True)
  similarity_new = similarity.join(ratings['评分次数'])
  similarity_new = similarity_new[similarity_new['评分次数'] > 20].sort_values(by='相关系数', ascending=False)
  similarity_new = similarity_new.iloc[0:10, 0]
  return similarity_new.index
