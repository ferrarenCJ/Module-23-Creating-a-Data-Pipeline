# Self-Study Discussion 23.1: Thinking Like a Data Scientist – Creating a Data Pipeline

## Discussion Post

One of the most valuable resources I found during this module was the official **Apache Airflow Documentation**.

**Resource:**
Apache Airflow Documentation

**Link:**
https://airflow.apache.org/docs/

**How It Helped**

Project 23.1 required building and executing a complete data pipeline within Apache Airflow running in Docker. While the course materials provided the overall project requirements, the Airflow documentation helped me better understand how workflows are organized through Directed Acyclic Graphs (DAGs), how operators are configured, and how task dependencies are managed. The documentation was particularly useful when troubleshooting task execution and understanding how Airflow schedules and orchestrates Python tasks.

Another helpful resource was the **BeautifulSoup Documentation**.

**Link:**
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

BeautifulSoup made it possible to parse the downloaded MIT course catalog HTML files and extract the course titles located within the `<h3>` tags. The examples in the documentation helped me understand methods such as `find_all()` and how HTML parsing works in practice.

Finally, I frequently referenced the **D3.js Gallery**.

**Link:**
https://observablehq.com/@d3/gallery

The gallery provided examples of various visualization techniques and helped me understand how D3 can transform raw JSON data into interactive visualizations. This was especially useful while modifying the bubble chart to display MIT course catalog word-frequency data.

These resources complemented the course materials and helped me successfully build an end-to-end sensemaking data pipeline that extracted, processed, analyzed, and visualized unstructured data.

---

## Peer Response Template 1

Thank you for sharing this resource. I also found documentation sites extremely helpful throughout Project 23.1 because they provide practical examples beyond the course material. Your recommendation for Apache Airflow documentation is particularly useful since understanding DAGs and task dependencies can be challenging for beginners. Were there any specific Airflow concepts or operators that you found especially helpful during the project?

---

## Peer Response Template 2

I enjoyed reading your discussion. The D3 Gallery is a great resource because seeing visualization examples makes it easier to understand what is possible beyond standard charts. I also found that studying example implementations helped reduce development time when building custom visualizations. Have you considered exploring other JavaScript visualization libraries such as Chart.js or Three.js for future projects?