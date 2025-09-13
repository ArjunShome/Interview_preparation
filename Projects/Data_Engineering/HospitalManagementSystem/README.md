# 🏥 Hospital Management System

This project is structured into **multiple sub-projects**, progressing from **basic use cases** to more **advanced implementations**.  
It is designed to explore different technologies step by step.

---

## 📌 Sub-Projects

### 1. **Basic**

#### ✅ Functional Requirements
1. Check the **maximum number of patients registered in real-time** for a given timeframe.  
   *(Timeframe can be decided by the developer for now)*  
2. Aggregate patient data and store it in a database with the following schema:
    |ID| DATE|START_TIME|END_TIME|PATIENT_COUNT

#### ⚙️ Non-Functional Requirements
- **Kafka** → for live streaming of data.  
- **PySpark** → for data transformation and aggregation.  
- **MongoDB** → for storing aggregated patient data.  

---

### 2. **Intermediate**  
*(To be defined – could expand into more complex data processing, dashboards, or additional APIs.)*

---

### 3. **Advanced**  
*(To be defined – could include ML-driven predictions, scaling with cloud infra, or microservice-based architecture.)*  

---

## 🚀 Tech Stack
- **Kafka** – Real-time data streaming  
- **PySpark** – Data transformation & aggregation  
- **MongoDB** – Database for storing processed data  

---

## 📂 Project Roadmap
- [ ] Implement **Basic Sub-Project** (Kafka + PySpark + MongoDB)  
- [ ] Extend to **Intermediate** use cases  
- [ ] Build **Advanced** capabilities  

---