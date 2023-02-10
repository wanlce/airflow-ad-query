#
# Copyright 2022 wano <whox@foxmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import setuptools

setuptools.setup(
    name="airflow_ad_query",
    version="0.1",
    author="wano",
    author_email="whox@foxmail.com",
    description="airflow ad query",
    url="https://github.com/wanlce/airflow-ad-query",
    license="Apahce",
    packages=setuptools.find_packages(),
    install_requires=["apache-airflow>= 2.0.0", "WTForms >= 2.3.3 "],
    entry_points={
        "airflow.plugins": [
            "airflow_ad_query=airflow_ad_query.ad_query:AirflowQueryPlugin"
        ]
    },
)
