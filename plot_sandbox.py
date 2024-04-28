import matplotlib.pyplot as plt
import matplotlib.ticker as tick

def sample_custom_ticks(major_ticks,minor_ticks,axis_limits,axis_scales):
    """shows off some different scales to give you an idea
    """
    def forward(x):
        return x**(1/3)

    def inverse(x):
        return x**3

    # start empty fig with several scale options
    num_scale_tests = len(axis_scales)
    fig,axes = plt.subplots(num_scale_tests,1,figsize=(18,8), layout='constrained')

    # for each graph, set axis limits and scale, then add ticks and title
    for i in range(0,num_scale_tests):
        ax = axes[i]
        ax.set_xlim(axis_limits)
        if axis_scales[i] == "function":
            ax.set_xscale(axis_scales[i],functions=(forward,inverse))
        else:
            ax.set_xscale(axis_scales[i])

        # set ticks at fixed locations with small ticks at 0.1 intervals
        ax.xaxis.set_major_locator(tick.FixedLocator(major_ticks))
        ax.xaxis.set_minor_locator(tick.FixedLocator(minor_ticks))
        ax.set_title(axis_scales[i])

    plt.show()

def exponential_scale_only(major_ticks,minor_ticks,axis_limits,exponent=3):
    """use this one--it's nice.
    """
    def forward(x):
        return x**(1/exponent)

    def inverse(x):
        return x**exponent

    # start empty fig and set limits + scale
    fig,ax = plt.subplots(figsize=(18,8), layout='constrained')
    ax.set_xlim(axis_limits)
    ax.set_xscale("function",functions=(forward,inverse))

    # set ticks at fixed locations with small ticks at 0.1 intervals
    #ax.xaxis.set_major_formatter('{x:0<6.1f}') #  is num characters in label, .1 is min precision
    ax.xaxis.set_major_locator(tick.FixedLocator(major_ticks))
    ax.xaxis.set_minor_locator(tick.FixedLocator(minor_ticks))
    ax.set_xticklabels([f"{label:.4f}" for label in major_ticks])
    ax.set_title("exponential scale: x^{0}".format(exponent))

    plt.show()

if __name__== "__main__":
    tick_loc = [0,0.0001, 0.001, 0.01, 0.1, 0.5, 0.9, 1]
    unmarked_tick_loc = [0.2,0.3,0.4,0.6,0.7,0.8]
    ax_lim = [0,1.1]
    show_multiple = False
    if show_multiple:
        ax_scale = ["symlog","log","linear","function"]
        sample_custom_ticks(tick_loc,unmarked_tick_loc,ax_lim,ax_scale)
    else:
        exponential_scale_only(tick_loc,unmarked_tick_loc,ax_lim,exponent=3)