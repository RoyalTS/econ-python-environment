import os


# The project root directory and the build directory.
top = '.'
out = 'bld'


def set_project_paths(ctx):
    """Define the project paths."""

    pp = {}
    # The PROJECT_ROOT path will be appended to the PYTHONPATH environmental
    # variable. Do the same in the Eclipse project settings, if applicable.
    pp['PROJECT_ROOT'] = '.'
    pp['SRC_EXAMPLES'] = 'src/examples'
    pp['BLD_EXAMPLES'] = '{}/src/examples'.format(out)

    # Convert the directories into waf nodes.
    for key, val in pp.items():
        pp[key] = ctx.path.make_node(val)

    return pp


def options(opt):
    opt.load('compiler_c')


def configure(ctx):
    ctx.env.PYTHONPATH = os.getcwd()
    ctx.load('sphinx_build')


def build(ctx):
    ctx.env.PROJECT_PATHS = set_project_paths(ctx)
    ctx.recurse('src')
