from bs4 import BeautifulSoup

html = """
<div data-v-d82d2bbe="" class="correlation-degree"><div data-v-d82d2bbe="" class="recruit-wrap recruit-margin"><!----> <div data-v-d82d2bbe="" class="recruit-list"><a data-v-d82d2bbe="" class="recruit-list-link"><h4 data-v-d82d2bbe="" class="recruit-title">CSIG16-python后台开发工程师（CSIG全资子公司）</h4> <p data-v-d82d2bbe="" class="recruit-tips">
                <span data-v-d82d2bbe="">CSIG</span> |
                  <span data-v-d82d2bbe="">武汉,中国</span> |
                  <span data-v-d82d2bbe="">技术</span> |
                  <span data-v-d82d2bbe="">腾讯位置服务</span> |
                   <span data-v-d82d2bbe="">2022年12月27日</span></p> <p data-v-d82d2bbe="" class="recruit-text">负责腾讯地图自研自动化工程设计、开发工作;
负责腾讯地图背景作业平台相关产品的技术研发支持；
负责编写相关的技术文档、单元测试，对产品质量负责；</p></a> <div data-v-c99c620c="" data-v-d82d2bbe="" class="recruit-share"><div data-v-c99c620c="" class="recruit-content"><span data-v-c99c620c="" class="share"></span> <span data-v-c99c620c="" class="share-text">分享</span> <div data-v-c99c620c="" id="share-detail" class="share-list"><div data-v-c99c620c="" class="share-title">分享</div> <div data-v-c99c620c="" class="close-btn"></div> <div data-v-c99c620c="" id="1595970048864821248" class="qr-code" style="display: none;"></div> <ul data-v-c99c620c="" class="share-gound"><li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon qq"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="javascript:;" class="share-icon wechat"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon micro-blog"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon in"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon facebook"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon twitter"></a></li></ul> <div data-v-c99c620c="" class="link-wrapper"><div data-v-c99c620c="" class="link-text">岗位链接</div> <div data-v-c99c620c="" class="link-ground"><input data-v-c99c620c="" readonly="readonly" id="" class="link input-text"> <div data-v-c99c620c="" class="copy">复制链接</div></div></div></div></div></div> <div data-v-d82d2bbe="" class="recruit-collection"><span data-v-d82d2bbe="" class="icon-collection"></span> <span data-v-d82d2bbe="" class="collection-text">收藏</span></div></div><div data-v-d82d2bbe="" class="recruit-list"><a data-v-d82d2bbe="" class="recruit-list-link"><h4 data-v-d82d2bbe="" class="recruit-title">CSIG17-WEB前端开发工程师（CSIG全资子公司)（西安）</h4> <p data-v-d82d2bbe="" class="recruit-tips"><span data-v-d82d2bbe="">CSIG</span> |
                  <span data-v-d82d2bbe="">西安,中国</span> |
                  <span data-v-d82d2bbe="">技术</span> |
                  <span data-v-d82d2bbe="">腾讯云</span> |
                   <span data-v-d82d2bbe="">2022年12月29日</span></p> <p data-v-d82d2bbe="" class="recruit-text">1、负责性能测试工具平台前端（WEB领域）界面开发。
2、参与架构、组件、模块化、规范化的制定和研发。
3、持续优化系统、框架、组件等。
注：此岗位位腾讯集团旗下全资子公司编制</p></a> <div data-v-c99c620c="" data-v-d82d2bbe="" class="recruit-share"><div data-v-c99c620c="" class="recruit-content"><span data-v-c99c620c="" class="share"></span> <span data-v-c99c620c="" class="share-text">分享</span> <div data-v-c99c620c="" id="share-detail" class="share-list"><div data-v-c99c620c="" class="share-title">分享</div> <div data-v-c99c620c="" class="close-btn"></div> <div data-v-c99c620c="" id="1587421898566803456" class="qr-code" style="display: none;"></div> <ul data-v-c99c620c="" class="share-gound"><li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon qq"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="javascript:;" class="share-icon wechat"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon micro-blog"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon in"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon facebook"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon twitter"></a></li></ul> <div data-v-c99c620c="" class="link-wrapper"><div data-v-c99c620c="" class="link-text">岗位链接</div> <div data-v-c99c620c="" class="link-ground"><input data-v-c99c620c="" readonly="readonly" id="" class="link input-text"> <div data-v-c99c620c="" class="copy">复制链接</div></div></div></div></div></div> <div data-v-d82d2bbe="" class="recruit-collection"><span data-v-d82d2bbe="" class="icon-collection"></span> <span data-v-d82d2bbe="" class="collection-text">收藏</span></div></div><div data-v-d82d2bbe="" class="recruit-list"><a data-v-d82d2bbe="" class="recruit-list-link"><h4 data-v-d82d2bbe="" class="recruit-title">25927-Senior Game Tester</h4> <p data-v-d82d2bbe="" class="recruit-tips"><span data-v-d82d2bbe="">IEG</span> |
                  <span data-v-d82d2bbe="">新加坡,新加坡</span> |
                  <span data-v-d82d2bbe="">技术</span> |
                  <!----> <span data-v-d82d2bbe="">2023年01月05日</span></p> <p data-v-d82d2bbe="" class="recruit-text">Responsible for ensure not only the quality of the game but also the quality of processes within the QA team;
Validate any changes and ensure that there are no issues; 
Create, monitor, and resolve bug reports as well as provide feedback to other QA in improving the quality of their reports; 
Define and promote quality standards in creating QA deliverables (Test Plans, Test Cases, Test reports, etc.) for the team; 
Ensure build stability by performing necessary tests and providing relevant reports that is clearly communicated within the team; 
Work with team leads to plan, schedule and ensure QA involvement in all phases of production; 
Collaborate with offsite teams and ensure QA team hit the objectives of the project; 
Communicate effectively, constructively, and efficiently any issues or topics to key Stakeholders, Directors, Production Teams in addition to the cell/QA group. Singapore-WeWork</p></a> <div data-v-c99c620c="" data-v-d82d2bbe="" class="recruit-share"><div data-v-c99c620c="" class="recruit-content"><span data-v-c99c620c="" class="share"></span> <span data-v-c99c620c="" class="share-text">分享</span> <div data-v-c99c620c="" id="share-detail" class="share-list"><div data-v-c99c620c="" class="share-title">分享</div> <div data-v-c99c620c="" class="close-btn"></div> <div data-v-c99c620c="" id="1611216000936583168" class="qr-code" style="display: none;"></div> <ul data-v-c99c620c="" class="share-gound"><li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon qq"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="javascript:;" class="share-icon wechat"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon micro-blog"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon in"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon facebook"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon twitter"></a></li></ul> <div data-v-c99c620c="" class="link-wrapper"><div data-v-c99c620c="" class="link-text">岗位链接</div> <div data-v-c99c620c="" class="link-ground"><input data-v-c99c620c="" readonly="readonly" id="" class="link input-text"> <div data-v-c99c620c="" class="copy">复制链接</div></div></div></div></div></div> <div data-v-d82d2bbe="" class="recruit-collection"><span data-v-d82d2bbe="" class="icon-collection"></span> <span data-v-d82d2bbe="" class="collection-text">收藏</span></div></div><div data-v-d82d2bbe="" class="recruit-list"><a data-v-d82d2bbe="" class="recruit-list-link"><h4 data-v-d82d2bbe="" class="recruit-title">NLP senior researcher</h4> <p data-v-d82d2bbe="" class="recruit-tips"><span data-v-d82d2bbe="">IEG</span> |
                  <span data-v-d82d2bbe="">新加坡,新加坡</span> |
                  <span data-v-d82d2bbe="">技术</span> |
                  
                  <!----> <span data-v-d82d2bbe="">2022年12月07日</span></p> <p data-v-d82d2bbe="" class="recruit-text">1. Design and build NLP algorithms for semantic analysis, intent recognition, chatbot, machine translation, knowledge graph, named-entity recognition.
2. Conduct research to advance the state of the art in NLP and create technical solutions at scale to real world challenges in various application scenarios.
3. Design and build NLP algorithms for semantic analysis, intent recognition, chatbot, machine translation, knowledge graph, named-entity recognition. Singapore-CapitalSpring | Singapore-WeWork</p></a> <div data-v-c99c620c="" data-v-d82d2bbe="" class="recruit-share"><div data-v-c99c620c="" class="recruit-content"><span data-v-c99c620c="" class="share"></span> <span data-v-c99c620c="" class="share-text">分享</span> <div data-v-c99c620c="" id="share-detail" class="share-list"><div data-v-c99c620c="" class="share-title">分享</div> <div data-v-c99c620c="" class="close-btn"></div> <div data-v-c99c620c="" id="1600737560106115072" class="qr-code" style="display: none;"></div> <ul data-v-c99c620c="" class="share-gound"><li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon qq"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="javascript:;" class="share-icon wechat"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon micro-blog"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon in"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon facebook"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon twitter"></a></li></ul> <div data-v-c99c620c="" class="link-wrapper"><div data-v-c99c620c="" class="link-text">岗位链接</div> <div data-v-c99c620c="" class="link-ground"><input data-v-c99c620c="" readonly="readonly" id="" class="link input-text"> <div data-v-c99c620c="" class="copy">复制链接</div></div></div></div></div></div> <div data-v-d82d2bbe="" class="recruit-collection"><span data-v-d82d2bbe="" class="icon-collection"></span> <span data-v-d82d2bbe="" class="collection-text">收藏</span></div></div><div data-v-d82d2bbe="" class="recruit-list"><a data-v-d82d2bbe="" class="recruit-list-link"><h4 data-v-d82d2bbe="" class="recruit-title">Quality Assurance Intern</h4> <p data-v-d82d2bbe="" class="recruit-tips"><span data-v-d82d2bbe="">IEG</span> |
                  <span data-v-d82d2bbe="">新加坡,新加坡</span> |
                  <span data-v-d82d2bbe="">技术</span> |
                  <!----> <span data-v-d82d2bbe="">2022年12月15日</span></p> <p data-v-d82d2bbe="" class="recruit-text">'- Responsible for quality control of the games. Propose, follow-up and implement test plans. Monitor projects' production quality and implement improvements.
- Gather and analyse product testing requirements. Explore more testing methodology and dimensions. Improve quality, efficiency and depth of testing process.</p></a> <div data-v-c99c620c="" data-v-d82d2bbe="" class="recruit-share"><div data-v-c99c620c="" class="recruit-content"><span data-v-c99c620c="" class="share"></span> <span data-v-c99c620c="" class="share-text">分享</span> <div data-v-c99c620c="" id="share-detail" class="share-list"><div data-v-c99c620c="" class="share-title">分享</div> <div data-v-c99c620c="" class="close-btn"></div> <div data-v-c99c620c="" id="1603418033303330816" class="qr-code" style="display: none;"></div> <ul data-v-c99c620c="" class="share-gound"><li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon qq"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="javascript:;" class="share-icon wechat"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon micro-blog"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon in"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon facebook"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon twitter"></a></li></ul> <div data-v-c99c620c="" class="link-wrapper"><div data-v-c99c620c="" class="link-text">岗位链接</div> <div data-v-c99c620c="" class="link-ground"><input data-v-c99c620c="" readonly="readonly" id="" class="link input-text"> <div data-v-c99c620c="" class="copy">复制链接</div></div></div></div></div></div> <div data-v-d82d2bbe="" class="recruit-collection"><span data-v-d82d2bbe="" class="icon-collection"></span> <span data-v-d82d2bbe="" class="collection-text">收藏</span></div></div><div data-v-d82d2bbe="" class="recruit-list"><a data-v-d82d2bbe="" class="recruit-list-link"><h4 data-v-d82d2bbe="" class="recruit-title">芯片后端工程师（深圳）</h4> <p data-v-d82d2bbe="" class="recruit-tips"><span data-v-d82d2bbe="">TEG</span> |
                  <span data-v-d82d2bbe="">深圳,中国</span> |
                  <span data-v-d82d2bbe="">技术</span> |
                  <!----> <span data-v-d82d2bbe="">2023年01月06日</span></p> <p data-v-d82d2bbe="" class="recruit-text">负责建立芯片后端设计流程，完成网表到GDS文件的交付，包括 FloorPlan、电源分配、时序优化、布局布线等；
配合前端设计工程师，完成low power 定义、SDC 编写、synthesis、LEC 等工作；
</p></a> <div data-v-c99c620c="" data-v-d82d2bbe="" class="recruit-share"><div data-v-c99c620c="" class="recruit-content"><span data-v-c99c620c="" class="share"></span> <span data-v-c99c620c="" class="share-text">分享</span> <div data-v-c99c620c="" id="share-detail" class="share-list"><div data-v-c99c620c="" class="share-title">分享</div> <div data-v-c99c620c="" class="close-btn"></div> <div data-v-c99c620c="" id="1547035269960572928" class="qr-code" style="display: none;"></div> <ul data-v-c99c620c="" class="share-gound"><li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon qq"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="javascript:;" class="share-icon wechat"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon micro-blog"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon in"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon facebook"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon twitter"></a></li></ul> <div data-v-c99c620c="" class="link-wrapper"><div data-v-c99c620c="" class="link-text">岗位链接</div> <div data-v-c99c620c="" class="link-ground"><input data-v-c99c620c="" readonly="readonly" id="" class="link input-text"> <div data-v-c99c620c="" class="copy">复制链接</div></div></div></div></div></div> <div data-v-d82d2bbe="" class="recruit-collection"><span data-v-d82d2bbe="" class="icon-collection"></span> <span data-v-d82d2bbe="" class="collection-text">收藏</span></div></div><div data-v-d82d2bbe="" class="recruit-list"><a data-v-d82d2bbe="" class="recruit-list-link"><h4 data-v-d82d2bbe="" class="recruit-title">Senior Machine Learning Engineer, ML Optimization - Lightspeed</h4> <p data-v-d82d2bbe="" class="recruit-tips"><span data-v-d82d2bbe="">IEG</span> |
                  <span data-v-d82d2bbe="">奥克兰,新西兰</span> |
                  <span data-v-d82d2bbe="">技术</span> |
                  <!----> <span data-v-d82d2bbe="">2022年12月21日</span></p> <p data-v-d82d2bbe="" class="recruit-text">- Participate in define the team's technical roadmap for ML model optimization
- Research, investigate and prototype model optimization techniques such as model quantization, compression or pruning to name a few
- Develop framework to seamlessly incorporate optimizations into existing model training pipelines as well as into online service UK-London | UK-Liverpool | Singapore-CapitalSpring | New Zealand-Remote</p></a> <div data-v-c99c620c="" data-v-d82d2bbe="" class="recruit-share"><div data-v-c99c620c="" class="recruit-content"><span data-v-c99c620c="" class="share"></span> <span data-v-c99c620c="" class="share-text">分享</span> <div data-v-c99c620c="" id="share-detail" class="share-list"><div data-v-c99c620c="" class="share-title">分享</div> <div data-v-c99c620c="" class="close-btn"></div> <div data-v-c99c620c="" id="1603002496559620096" class="qr-code" style="display: none;"></div> <ul data-v-c99c620c="" class="share-gound"><li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon qq"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="javascript:;" class="share-icon wechat"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon micro-blog"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon in"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon facebook"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon twitter"></a></li></ul> <div data-v-c99c620c="" class="link-wrapper"><div data-v-c99c620c="" class="link-text">岗位链接</div> <div data-v-c99c620c="" class="link-ground"><input data-v-c99c620c="" readonly="readonly" id="" class="link input-text"> <div data-v-c99c620c="" class="copy">复制链接</div></div></div></div></div></div> <div data-v-d82d2bbe="" class="recruit-collection"><span data-v-d82d2bbe="" class="icon-collection"></span> <span data-v-d82d2bbe="" class="collection-text">收藏</span></div></div><div data-v-d82d2bbe="" class="recruit-list"><a data-v-d82d2bbe="" class="recruit-list-link"><h4 data-v-d82d2bbe="" class="recruit-title">Backend Software Engineer Intern</h4> <p data-v-d82d2bbe="" class="recruit-tips"><span data-v-d82d2bbe="">IEG</span> |
                  <span data-v-d82d2bbe="">新加坡,新加坡</span> |
                  <span data-v-d82d2bbe="">技术</span> |
                  <!----> <span data-v-d82d2bbe="">2022年12月16日</span></p> <p data-v-d82d2bbe="" class="recruit-text">'- Design and implement account service modules.
- Design and implement related management system and tool-chain software.
- Maintain the online service system, and solve the problems effectively.
- Build backend systems and take charge of documenting requirements and specifications.</p></a> <div data-v-c99c620c="" data-v-d82d2bbe="" class="recruit-share"><div data-v-c99c620c="" class="recruit-content"><span data-v-c99c620c="" class="share"></span> <span data-v-c99c620c="" class="share-text">分享</span> <div data-v-c99c620c="" id="share-detail" class="share-list"><div data-v-c99c620c="" class="share-title">分享</div> <div data-v-c99c620c="" class="close-btn"></div> <div data-v-c99c620c="" id="1603594798428594176" class="qr-code" style="display: none;"></div> <ul data-v-c99c620c="" class="share-gound"><li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon qq"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="javascript:;" class="share-icon wechat"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon micro-blog"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon in"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon facebook"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon twitter"></a></li></ul> <div data-v-c99c620c="" class="link-wrapper"><div data-v-c99c620c="" class="link-text">岗位链接</div> <div data-v-c99c620c="" class="link-ground"><input data-v-c99c620c="" readonly="readonly" id="" class="link input-text"> <div data-v-c99c620c="" class="copy">复制链接</div></div></div></div></div></div> <div data-v-d82d2bbe="" class="recruit-collection"><span data-v-d82d2bbe="" class="icon-collection"></span> <span data-v-d82d2bbe="" class="collection-text">收藏</span></div></div><div data-v-d82d2bbe="" class="recruit-list"><a data-v-d82d2bbe="" class="recruit-list-link"><h4 data-v-d82d2bbe="" class="recruit-title">CSIG17-大数据系统测试工程师（CSIG全资子公司）（武汉/长沙/西安）</h4> <p data-v-d82d2bbe="" class="recruit-tips"><span data-v-d82d2bbe="">CSIG</span> |
                  <span data-v-d82d2bbe="">西安,中国</span> |
                  <span data-v-d82d2bbe="">技术</span> |
                  <span data-v-d82d2bbe="">腾讯云</span> |
                   <span data-v-d82d2bbe="">2022年12月14日</span></p> <p data-v-d82d2bbe="" class="recruit-text">负责大数据hadoop，spark，ES, hive，flink，clickhouse以及数据湖等相关产品的测试工作； 
分析产品相关需求、设计、架构等，设计测试方法和测试用例；
挖掘并跟进实施性能测试、竞品对比测试、稳定性等专项测试，保障和提升产品质量； 
负责建设产品相关的自动化测试、Devops等工作；
不断改进测试过程、方法和技术，提升产品质量。
注：此岗位为腾讯集团旗下全资子公司编制岗位</p></a> <div data-v-c99c620c="" data-v-d82d2bbe="" class="recruit-share"><div data-v-c99c620c="" class="recruit-content"><span data-v-c99c620c="" class="share"></span> <span data-v-c99c620c="" class="share-text">分享</span> <div data-v-c99c620c="" id="share-detail" class="share-list"><div data-v-c99c620c="" class="share-title">分享</div> <div data-v-c99c620c="" class="close-btn"></div> <div data-v-c99c620c="" id="1513460517769846784" class="qr-code" style="display: none;"></div> <ul data-v-c99c620c="" class="share-gound"><li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon qq"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="javascript:;" class="share-icon wechat"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon micro-blog"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon in"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon facebook"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon twitter"></a></li></ul> <div data-v-c99c620c="" class="link-wrapper"><div data-v-c99c620c="" class="link-text">岗位链接</div> <div data-v-c99c620c="" class="link-ground"><input data-v-c99c620c="" readonly="readonly" id="" class="link input-text"> <div data-v-c99c620c="" class="copy">复制链接</div></div></div></div></div></div> <div data-v-d82d2bbe="" class="recruit-collection"><span data-v-d82d2bbe="" class="icon-collection"></span> <span data-v-d82d2bbe="" class="collection-text">收藏</span></div></div><div data-v-d82d2bbe="" class="recruit-list"><a data-v-d82d2bbe="" class="recruit-list-link"><h4 data-v-d82d2bbe="" class="recruit-title">25928-图计算高级工程师</h4> <p data-v-d82d2bbe="" class="recruit-tips"><span data-v-d82d2bbe="">IEG</span> |
                  <span data-v-d82d2bbe="">深圳,中国</span> |
                  <span data-v-d82d2bbe="">技术</span> |
                  <!----> <span data-v-d82d2bbe="">2022年11月28日</span></p> <p data-v-d82d2bbe="" class="recruit-text">分析网络传输测试数据，为业务调度提供准确指导信息，提高网络传输优化效率；
分析网络传输连通性，及时发现故障点以及最优路径，降低网络故障对网络用户的影响。</p></a> <div data-v-c99c620c="" data-v-d82d2bbe="" class="recruit-share"><div data-v-c99c620c="" class="recruit-content"><span data-v-c99c620c="" class="share"></span> <span data-v-c99c620c="" class="share-text">分享</span> <div data-v-c99c620c="" id="share-detail" class="share-list"><div data-v-c99c620c="" class="share-title">分享</div> <div data-v-c99c620c="" class="close-btn"></div> <div data-v-c99c620c="" id="1582280939684241408" class="qr-code" style="display: none;"></div> <ul data-v-c99c620c="" class="share-gound"><li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon qq"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="javascript:;" class="share-icon wechat"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon micro-blog"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon in"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon facebook"></a></li> <li data-v-c99c620c="" class="share-item"><a data-v-c99c620c="" href="" target="_blank" class="share-icon twitter"></a></li></ul> <div data-v-c99c620c="" class="link-wrapper"><div data-v-c99c620c="" class="link-text">岗位链接</div> <div data-v-c99c620c="" class="link-ground"><input data-v-c99c620c="" readonly="readonly" id="" class="link input-text"> <div data-v-c99c620c="" class="copy">复制链接</div></div></div></div></div></div> <div data-v-d82d2bbe="" class="recruit-collection"><span data-v-d82d2bbe="" class="icon-collection"></span> <span data-v-d82d2bbe="" class="collection-text">收藏</span></div></div></div></div>
"""
soup = BeautifulSoup(html, "lxml")

# 美化html
# print(bs.prettify())

# 打印所有span标签
# span = soup.find_all('span')
# for sp in span:
#     print(sp)
#     print(type(sp))

# 获取第二个span标签
# sp_2 = soup.find_all('span', limit=2)[1]
# print(sp_2)

# 获取所有class等于recruit-text的p标签
# p = soup.find_all('p', attrs={'class': "recruit-text"})
# 也可以写成
# p = soup.find_all('p', class_='recruit-text')
# for rp in p:
#     print(rp)
#     print("="*30)

