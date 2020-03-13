<!--
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->


#简历抽取基本流程

##0. 爬取数据

##1. 文本清洗

##2. 文本分块，找出 JD 的文本块

##3. keyword 抽取
  ###3.1 基于 Rake 的关键词抽取
  ###3.2 基于模型 LSTM-CRT 的关键词抽取

##4. 句法分析，抽取职位描述结构.

##5. 输出 json 结果，以 js 展示.