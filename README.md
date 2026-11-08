<div align="center">

# 云网络：从隔离到连接

### 从物理网络到云原生网络的演进之旅

<p>
  <a href="https://caozhiyi.github.io/network-book/"><img src="https://img.shields.io/badge/📖_在线阅读-mkdocs-2196F3?style=for-the-badge" alt="在线阅读"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey?style=for-the-badge" alt="License"></a>
</p>

</div>

---

**云网络的每一个产品，都是被某个约束逼出来的解法。**

这本书要做的事情，是把这个“逼出来”的过程完整地展示给你看。全书从最朴素的问题开始——两台机器怎么通信。然后机器变多了，广播域炸了；多个租户共用一张网，互相干扰；VLAN 的 4096 上限撑不住云的规模；VxLAN 解决了隔离但引入了 VTEP 的落点问题……每一章解决上一章遗留的问题，每一章的解法又引入新的约束，催生下一章的问题。

这是一条从物理网络边界出发，历经多租户隔离、VPC内部通信、公网连接、VPC互联、混合云、全球加速、安全防护、可观测与流量治理的因果链。

---

## 📖 在线阅读

**🌐 推荐方式：[在线版（mkdocs）](https://caozhiyi.github.io/network-book/)** — 提供完整的目录导航、暗黑模式和清晰的系统结构配图。

也可以直接点击下方目录跳转到 GitHub 上的对应章节。

---

## 📚 全书结构：约束链的九次跃迁

全书 **9 卷 31 章**，通过真实的演进链条揭示云网络的底层原理。

<details>
<summary><b>📘 卷一：物理网络的边界</b> · 物理拓扑 · 广播域限制 · 大二层瓶颈</summary>

| 章 | 标题 |
|---|---|
| 0 | [卷一导读：物理网络的边界](docs/00a.卷一导读物理网络的边界.md) |
| 1 | [一根网线两头是谁: 最底层的直接通信](docs/01.一根网线两头是谁.md) |
| 2 | [十万台机器的网络: 广播风暴与大规模组网](docs/02.十万台机器的网络.md) |

</details>

<details>
<summary><b>📗 卷二：多租户隔离</b> · VLAN 边界 · Overlay 网络 · VxLAN · VTEP 落点</summary>

| 章 | 标题 |
|---|---|
| 0 | [卷二导读：多租户隔离](docs/02a.卷二导读多租户隔离.md) |
| 3 | [共用网络的噩梦: 隔离性与安全性的第一层挑战](docs/03.共用网络的噩梦.md) |
| 4 | [VLAN的边界: 4096 限制与硬隔离的终结](docs/04.VLAN的边界.md) |
| 5 | [给包裹再套一层: VxLAN 与 Overlay 网络的诞生](docs/05.给包裹再套一层VxLAN与Overlay网络.md) |
| 6 | [Tunnel在哪里终止: VTEP 的落点与隧道解包](docs/06.Tunnel在哪里终止VTEP的落点.md) |

</details>

<details>
<summary><b>📙 卷三：VPC 内部通信</b> · 分布式网关 · 三层路由 · 安全组 · ARP 代答 · 容器网络</summary>

| 章 | 标题 |
|---|---|
| 0 | [卷三导读：VPC内部通信](docs/07a.卷三导读VPC内部通信.md) |
| 7 | [VPC是什么: 从网络技术到云产品的蜕变](docs/07.VPC是什么从网络技术到云产品.md) |
| 8 | [同一个子网内的通信: ARP 代答与虚拟交换机封包](docs/08.同一个子网内的通信ARP代答与封包.md) |
| 9 | [跨子网通信: 分布式网关与三层路由的折中](docs/09.跨子网通信分布式网关与三层路由.md) |
| 10 | [谁来守门: 安全组与网络 ACL 的两道防线](docs/10.谁来守门安全组与网络ACL.md) |
| 11 | [VPC内的基础网络服务: DHCP、DNS、元数据与 ENI](docs/11.VPC内的基础网络服务DHCP与DNS与元数据与弹性网卡.md) |
| 12 | [容器加入VPC: Pod 如何直通 VPC 网络](docs/12.容器加入VPC之Pod如何获得VPC_IP.md) |

</details>

<details>
<summary><b>📕 卷四：公网连接</b> · NAT 网关 · 弹性公网 IP (EIP) · 负载均衡 (SLB)</summary>

| 章 | 标题 |
|---|---|
| 0 | [卷四导读：公网连接](docs/12a.卷四导读公网连接.md) |
| 13 | [VM要上网: 出公网 SNAT 与网关吞吐边界](docs/13.VM要上网NAT网关的诞生.md) |
| 14 | [固定的公网身份: 弹性公网 IP (EIP) 的路由宣告](docs/14.固定的公网身份弹性公网IP.md) |
| 15 | [流量涌入一台撑不住: 四层与七层负载均衡架构](docs/15.流量涌入一台撑不住负载均衡.md) |

</details>

<details>
<summary><b>📔 卷五：VPC 互联</b> · 对等连接 (Peering) · 云联网 (CCN) · PrivateLink</summary>

| 章 | 标题 |
|---|---|
| 0 | [卷五导读：VPC互联](docs/15a.卷五导读VPC互联.md) |
| 16 | [两个VPC之间拉一条线: 对等连接与路由表网流](docs/16.两个VPC之间拉一条线对等连接.md) |
| 17 | [VPC互联的总线: 云联网的路由收敛与网状拓扑](docs/17.VPC互联的总线云联网.md) |
| 18 | [地址冲突也要互访问: PrivateLink 跨租户单向路由](docs/18.地址冲突也要互访PrivateLink.md) |

</details>

<details>
<summary><b>📓 卷六：混合云网络</b> · IPsec VPN · 物理专线 · 云联网纵向扩展</summary>

| 章 | 标题 |
|---|---|
| 0 | [卷六导读：混合云网络](docs/18a.卷六导读混合云网络.md) |
| 19 | [用互联网打通云和IDC: VPN 连接与加密网关](docs/19.用互联网打通云和IDC之VPN连接.md) |
| 20 | [拉一根光纤: 专线接入与边界路由器(VBR)划分子接口](docs/20.拉一根光纤专线接入.md) |
| 21 | [统一管理云和IDC的连接: 云联网的纵向扩展](docs/21.统一管理云和IDC的连接云联网的纵向扩展.md) |

</details>

<details>
<summary><b>📒 卷七：全球接入与加速</b> · GSLB · Anycast · 云骨干网 · CDN 边缘</summary>

| 章 | 标题 |
|---|---|
| 0 | [卷七导读：全球接入与加速](docs/21a.卷七导读全球接入与加速.md) |
| 22 | [全球用户如何找到最近的服务: DNS 与全局负载均衡 GSLB](docs/22.全球用户如何找到最近的服务DNS与GSLB.md) |
| 23 | [让流量走更好的路: Anycast 路由宣告与云骨干网多径优化](docs/23.让流量走更好的路Anycast与云骨干网.md) |
| 24 | [把内容推到用户身边: CDN 缓存架构与边缘计算节点](docs/24.把内容推到用户身边CDN与边缘节点.md) |

</details>

<details>
<summary><b>📓 卷八：流量安全防护</b> · DDoS 流量清洗 · 流量黑洞 · WAF 层过滤</summary>

| 章 | 标题 |
|---|---|
| 0 | [卷八导读：流量安全防护](docs/24a.卷八导读流量安全防护.md) |
| 25 | [洪水来袭: DDoS 防护与Anycast任播清洗](docs/25.洪水来袭DDoS防护.md) |
| 26 | [伪装成正常请求的攻击: WAF 与应用层精细化过滤](docs/26.伪装成正常请求的攻击WAF与应用层防护.md) |

</details>

<details>
<summary><b>📗 卷九：可观测与流量治理</b> · 流日志 · 主动探测 · 网络层容灾 · eBPF/服务网格</summary>

| 章 | 标题 |
|---|---|
| 0 | [卷九导读：可观测与流量治理](docs/26a.卷九导读可观测与流量治理.md) |
| 27 | [出了问题从哪查起: VPC Flow Logs 的生成与投递](docs/27.出了问题从哪查起网络流日志.md) |
| 28 | [在用户感知之前发现故障: 主动探测与端到端拨测系统](docs/28.在用户感知之前发现故障主动探测.md) |
| 29 | [故障时如何自救: 多路径备用路由与网络层快速收敛](docs/29.故障时如何自救多路径与网络层容灾.md) |
| 30 | [微服务的流量治理: 服务网格(Service Mesh)与 eBPF 的无侵入控制](docs/30.微服务的流量治理服务网格与eBPF.md) |

</details>

<details>
<summary><b>📓 后记</b> · 根本性约束</summary>

| 章 | 标题 |
|---|---|
| - | [后记：云网络的下一个根本性约束](docs/32.后记云网络的下一个根本性约束.md) |

</details>

---

## 🧭 适合谁读

- **云网络的使用者**：经常与 VPC、安全组、NAT 网关打交道，想穿透黑盒理解其设计动机与资源限制的云上架构师和后端开发。
- **网络工程师转云方向**：熟悉传统设备与二三层协议，但想迅速弄明白 VxLAN、分布式网关以及 SDN 控制面究竟带来了什么颠覆的工程师。
- **混合云/分布式架构师**：负责专线、云联网、全球加速选型，需要在可用性、成本和网络复杂度之间做决策的架构师。

> ⚠️ **注意**：本书不包含各家云厂商的控制台操作截图或配置命令，也未提供代码实现。本书聚焦于**架构演进、产品逻辑和设计哲学**。

---

## 🛠️ 本地预览

如果你想在本地编译并预览 MkDocs 页面：

```bash
# 安装依赖
pip install -r requirements.txt

# 本地启动服务器预览
mkdocs serve
```
启动后在浏览器打开 `http://127.0.0.1:8000` 即可。

---

## 🌟 关于作者

我是 **caozhiyi**，多年网络与分布式系统架构从业者。

> 📮 公众号：**煮码宝藏** — 持续分享网络协议底层、高并发异步系统设计及分布式网络架构实践。

---

## 🤝 参与与反馈

- 🐛 文字纰漏或概念谬误 → [提 Issue](https://github.com/caozhiyi/network-book/issues)
- 💡 对演进脉络有更好的想法 → [提 PR](https://github.com/caozhiyi/network-book/pulls)
- ⭐ 觉得有用？**Star 是对作者最大的鼓励**

---

## 📜 版权协议

本书采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 协议。允许署名、非商业性使用和相同方式分享。
