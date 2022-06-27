# Copyright 2022 CRS4.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
# of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""\
Generate a Workflow Testing RO-Crate from a "best practices" Nextflow
workflow repository.

https://nf-co.re/contributing/guidelines
https://nf-co.re/developers/adding_pipelines#nf-core-pipeline-structure
"""

from .common import CrateBuilder


WF_BASENAME = "main.nf"


def find_workflow(root_dir):
    wf_path = root_dir / WF_BASENAME
    if not wf_path.is_file():
        raise RuntimeError(f"{wf_path} not found")
    return wf_path


class NextflowCrateBuilder(CrateBuilder):

    CI_WORKFLOW = "ci.yml"
    DATA_ENTITIES = [
        ("assets", "Dataset", "Additional files"),
        ("bin", "Dataset", "Scripts that must be callable from a pipeline process"),
        ("conf", "Dataset", "Configuration files"),
        ("docs", "Dataset", "Markdown files for documenting the pipeline"),
        ("docs/images", "Dataset", "Images for the documentation files"),
        ("lib", "Dataset", "Groovy utility functions"),
        ("modules", "Dataset", "Modules used by the pipeline"),
        ("modules/local", "Dataset", "Pipeline-specific modules"),
        ("modules/nf-core", "Dataset", "nf-core modules"),
        ("workflows", "Dataset", "Main pipeline workflows to be executed in main.nf"),
        ("subworkflows", "Dataset", "Smaller subworkflows"),
        ("nextflow.config", "File", "Main Nextflow configuration file"),
        ("README.md", "File", "Basic pipeline usage information"),
        ("nextflow_schema.json", "File", "JSON schema for pipeline parameter specification"),
        ("CHANGELOG.md", "File", "Information on changes made to the pipeline"),
        ("LICENSE", "File", "The license - should be MIT"),
        ("CODE_OF_CONDUCT.md", "File", "The nf-core code of conduct"),
        ("CITATIONS.md", "File", "Citations needed when using the pipeline"),
        ("modules.json", "File", "Version information for modules from nf-core/modules"),
    ]

    @property
    def lang(self):
        return "nextflow"


def make_crate(root, workflow=None, repo_url=None, wf_version=None, lang_version=None,
               license=None, ci_workflow=None, diagram=None):
    builder = NextflowCrateBuilder(root, repo_url=repo_url)
    if not workflow:
        workflow = find_workflow(root)
    return builder.build(workflow, wf_version=wf_version, lang_version=lang_version, license=license, ci_workflow=ci_workflow, diagram=diagram)
