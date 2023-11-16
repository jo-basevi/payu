"""Run the `payu checkout` command.

:copyright: Copyright 2018 Marshall Ward, see AUTHORS for details.
:license: Apache License, Version 2.0, see LICENSE for details.
"""
from pathlib import Path

from payu.laboratory import Laboratory
from payu.branch import checkout_branch
import payu.subcommands.args as args

title = 'checkout'
parameters = {'description': ('A wrapper around git checkout. '
                              'Create a new branch (if specified), '
                              'checkout branch, setup experiment metadata '
                              'and create/switch archive/work symlinks')}

arguments = [args.model, args.config, args.laboratory, args.new_branch,
             args.branch_name, args.start_point, args.restart_path]


def transform_strings_to_path(path_str=None):
    return Path(path_str) if path_str is not None else None


def runcmd(model_type, config_path, lab_path, new_branch,
           branch_name, start_point, restart_path):
    """Execute the command."""
    lab = Laboratory(model_type, config_path, lab_path)

    config_path = transform_strings_to_path(config_path)
    lab_path = transform_strings_to_path(lab_path)

    checkout_branch(lab=lab,
                    is_new_branch=new_branch,
                    branch_name=branch_name,
                    start_point=start_point,
                    restart_path=restart_path,
                    config_path=config_path)


runscript = runcmd
