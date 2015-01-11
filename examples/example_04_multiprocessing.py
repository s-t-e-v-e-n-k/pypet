__author__ = 'Robert Meyer'


from pypet import Environment, cartesian_product
from pypet import pypetconstants


# Let's reuse the simple multiplication example
def multiply(traj):
    """Sophisticated simulation of multiplication"""
    z=traj.x*traj.y
    traj.f_add_result('z',z=z, comment='I am the product of two reals!')



def main():
    """Main function to protect the *entry point* of the program.

    If you want to use multiprocessing under Windows you need to wrap your
    main code creating an environment into a function. Otherwise
    the newly started child processes will re-execute the code and throw
    errors (also see https://docs.python.org/2/library/multiprocessing.html#windows).

    """

    # Create an environment that handles running.
    # Let's enable multiprocessing with 2 workers.
    env = Environment(trajectory='Example_04_MP',
                      filename='experiments/example_04/HDF5/example_04.hdf5',
                      file_title='Example_04_MP',
                      log_folder='experiments/example_04/LOGS/',
                      comment = 'Multiprocessing example!',
                      multiproc=True,
                      ncores=2,
                      use_pool=True,
                      wrap_mode=pypetconstants.WRAP_MODE_LOCK)

    # Get the trajectory from the environment
    traj = env.v_trajectory

    # Add both parameters
    traj.f_add_parameter('x', 1.0, comment='I am the first dimension!')
    traj.f_add_parameter('y', 1.0, comment='I am the second dimension!')

    # Explore the parameters with a cartesian product, but we want to explore a bit more
    traj.f_explore(cartesian_product({'x':[float(x) for x in range(12)],
                                      'y':[float(y) for y in range(12)]}))

    # Run the simulation
    env.f_run(multiply)

if __name__ == '__main__':
    # This will execute the main function in case the script is called from the one true
    # main process and not from a child processes spawned by your environment.
    # Necessary for multiprocessing under Windows.
    main()