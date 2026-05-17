# langgraph_study
it's summarization written with my opinion and source is from langchain teddynote.
This site is written for my own study and source is from langchain teddynote (site will be written on bottom).
Just in case i'm  telling you, My study workflow will contain lots of korean.(actually all of them)

There is two folder, langchain basic folder and langgraph basic folder

## Before Starting
Be sure that this github is written for my own study summary.
Each file will be written in ipynb file.
All words will be written in korean.
it requires langchain library, (pip install langchain)
But for sure you could refer to requirements.txt

And my python version is 3.11.

## langchain basic folder is literally basic knowledge of langchain

it's composed with below lists.
(will not be written maybe)

and langgraph basic folder is composed with langgraph_basic, langgraph_little_advance, langgraph_examples

## first langgraph_basic file is composed with below lists.

- 용어를 정리 -- TypedDict, Annotated, add_messages
- 간단한 챗봇 구축 -- 상태 정의, 챗봇 노드, 빌더 구축, 그래프 생성, 간단 streaming 까지
- tool 사용
- memory 사용
- 여러 stream mode 사용 
- interrupt 시도
- interrupt 실제 사용
- 중간 개입을 실제 사람의 입력으로 -- 구현은 모자람
- 메세지를 삭제
- ToolNode 따로 이용 -- low level에서 ToolNode를 보기 위함
- 병렬 실행을 위한 분기 -- fan-in, fan-out의 기초를 공부
- 대화 요약 생성
- subgraph 추가 및 사용 방법
- subgraph들과 본 graph와의 연결

## second. langgraph_little_advance is composed with below lists.
- NAIVE RAG -- 실제 pdf를 retrieve해서 llm이 답변하는 간단 RAG를 구현
- 관련성 체크 노드 추가 -- retrieve된 docs와 question간의 관련성 간단 체크
- 웹 검색 노드 추가
- 쿼리 재작성 노드 추가
- agentic RAG
- adaptive RAG

## third. langgraph_examples file is composed with below lists.
- agent + simulated user graph -- 상황을 주고 llm과 둘이 해결하도록 (실제 해결까진 아닌) 하는 상황 만들기
- 사용자가 원하는 프롬프트 만들기 -- 필요한 정보를 받고 prompt를 쓰도록
- CRAG(corrective RAG) -- 문서를 retrieve해서 document grading + websearch + query rewrite까지 해보기
- self-RAG -- 순환(보완)이 있는 RAG 형식으로 실제 langgraph_little_advance의 adaptive RAG에 나오는 내용들
- plan and Execute -- 계획을 수립하고 그에 맞춰서 실행을 하는 RAG 만들기
- multi agent collaboration network -- 2개의 에이전트(모델+툴 을 기본으로 가진)를 서로 연결해서 결과 도출하기
- multi agent supervisor -- 위의 network를 관리하는 팀 supervisor를 포함한 RAG 만들기
- hierarical multi agent team -- 위에서 만들 'multi agent team'을 여러개 만들어서 그걸 관리하는 supervisor를 포함해서 RAG 만들기

모든 내용은 langchain teddynote를 기반으로 적어서 내용이 곂칠수 있으며 제 공부상 개인적인 생각이 들어가서 실제와 다를 수 있습니다.

출처: https://wikidocs.net/book/14314
