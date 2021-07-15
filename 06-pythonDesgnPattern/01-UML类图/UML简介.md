每个模式都有相应的对象结构图，同时为了展示对象间的交互细节， 有些时候会用到 UML 图来介绍其如何运行。这里不会将 UML 的各种元素都提到，只想讲讲类图中各个类之间的关系， 能看懂类图中各个类之间的线条、箭头代表什么意思后，也就足够应对日常的工作和交流。同时，我们应该能将类图所表达的含义和最终的代码对应起来。有了这些知识，看后面章节的设计模式结构图就没有什么问题了。

本文中大部分是 UML 类图，也有个别简易流程图。由于文中部分模式并未配图，你可以在[这里](https://github.com/xietao3/Study-Plan/tree/master/DesignPatterns/UML)查看我在网络上收集的完整 23 种设计模式 UML 类图。

###  继承

继承用一条带空心箭头的直接表示。



![img](https://raw.githubusercontent.com/xietao3/Study-Plan/master/DesignPatterns/src/%E7%BB%A7%E6%89%BF.png)



### 实现

实现关系用一条带空心箭头的虚线表示。



![img](https://raw.githubusercontent.com/xietao3/Study-Plan/master/DesignPatterns//src/%E5%AE%9E%E7%8E%B0.png)



### 组合

与聚合关系一样，组合关系同样表示整体由部分构成的语义。比如公司由多个部门组成，但组合关系是一种强依赖的特殊聚合关系，如果整体不存在了，则部分也不存在了。例如，公司不存在了，部门也将不存在了。



![img](https://raw.githubusercontent.com/xietao3/Study-Plan/master/DesignPatterns//src/%E7%BB%84%E5%90%88.png)



### 聚合

聚合关系用于表示实体对象之间的关系，表示整体由部分构成的语义，例如一个部门由多个员工组成。与组合关系不同的是，整体和部分不是强依赖的，即使整体不存在了，部分仍然存在。例如，部门撤销了，人员不会消失，他们依然存在。



![img](https://raw.githubusercontent.com/xietao3/Study-Plan/master/DesignPatterns/src/%E8%81%9A%E5%90%88.png)



### 关联

关联关系是用一条直线表示的，它描述不同类的对象之间的结构关系，它是一种静态关系， 通常与运行状态无关，一般由常识等因素决定的。它一般用来定义对象之间静态的、天然的结构， 所以，关联关系是一种“强关联”的关系。

比如，乘车人和车票之间就是一种关联关系，学生和学校就是一种关联关系，关联关系默认不强调方向，表示对象间相互知道。如果特别强调方向，如下图，表示 A 知道 B ，但 B 不知道 A 。



![img](https://raw.githubusercontent.com/xietao3/Study-Plan/master/DesignPatterns/src/%E5%85%B3%E8%81%94.png)



### 依赖

依赖关系是用一套带箭头的虚线表示的，如A依赖于B，他描述一个对象在运行期间会用到另一个对象的关系。

与关联关系不同的是，它是一种临时性的关系，通常在运行期间产生，并且随着运行时的变化，依赖关系也可能发生变化。显然，依赖也有方向，双向依赖是一种非常糟糕的结构，我们总是应该保持单向依赖，杜绝双向依赖的产生。



![img](https://raw.githubusercontent.com/xietao3/Study-Plan/master/DesignPatterns/src/%E4%BE%9D%E8%B5%96.png)

### 举例

请看以下这个类图，类之间的关系是我们需要关注的：

![_images/uml_class_struct.jpg](https://design-patterns.readthedocs.io/zh_CN/latest/_images/uml_class_struct.jpg)

- 车的类图结构为<<abstract>>，表示车是一个抽象类；
- 它有两个继承类：小汽车和自行车；它们之间的关系为实现关系，使用带空心箭头的虚线表示；
- 小汽车为与SUV之间也是继承关系，它们之间的关系为泛化关系，使用带空心箭头的实线表示；
- 小汽车与发动机之间是组合关系，使用带实心箭头的实线表示；
- 学生与班级之间是聚合关系，使用带空心箭头的实线表示；
- 学生与身份证之间为关联关系，使用一根实线表示；
- 学生上学需要用到自行车，与自行车是一种依赖关系，使用带箭头的虚线表示；

