# 텍스트 데이터 기반 기상 피해 문장 추출

### Motivation
* 본 프로젝트에서는 기사별 기상 피해 측정에 대한 선행 연구로, 기사 별 피해 문장을 추출하고자 한다. 이를 통해 영향 예보에 필요한 피해 현황 정보를 수집하는 것을 목표로 한다. 여러 데이터 마이닝 기법을 사용하여 최적의 분류 모델을 생성한 뒤 실제 데이터에 적용해 정성적인 평가를 진행하였다.

### Data
* 기상 피해 관련 기사를 수집하기 위해 대표적인 기상 재해인 ‘폭염’과 ‘대설’이라는 키워드를 대상으로 기사를 수집했다. ‘폭염’ 키워드에 대해서는 한국언론진흥재단의 빅카인즈(BIG KINDS) 기사 제공 플랫폼에서 주요 52개 언론사에 대해 수집했다. 이후에 NAVER 뉴스 서비스 플랫폼에서 (앞에서 사용된 주요 언론사를 제외한) 추가적인 52개 언론사를 통해 기사 수집을 하였다. ‘대설’ 키워드에 대해서는 NAVER 뉴스 서비스 플랫폼에서 총 104개 언론사에 대해 일괄 수집하였다. 
* 수집된 데이터에 대해 기상 피해와 관련 정도를 점수로 매겨, 여러 문장들을 피해 관련 문장으로 분류하였다.

### Method & Tools
* Word Embedding(Word2vec, Doc2vec, FastText)
* XGBoost
* LSTM
* 1D-CNN
* [Associative Classification based on Transferable belief Model](https://www.sciencedirect.com/science/article/pii/S0950705119302758)
