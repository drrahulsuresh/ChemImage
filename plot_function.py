import matplotlib.pyplot as plt

def apply_plot_formatting(ax):
    """
    General function to format any matplotlib plot.
    Applies settings for spines, fonts, and other formatting preferences.
    """
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.xaxis.label.set_fontname('Arial')
    ax.yaxis.label.set_fontname('Arial')
    ax.xaxis.label.set_fontsize(16)
    ax.yaxis.label.set_fontsize(16)

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontname('Arial')
        label.set_fontsize(16)
    ax.set_title('')

    legend = ax.get_legend()
    if legend:
        legend.prop.set_family('Arial')
        legend.frameon = False  
        legend.set_title('')

def plot_roc_curve(fpr, tpr, roc_auc):
    """
    Function to plot the ROC curve with customized formatting.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(fpr, tpr, color='blue', linewidth=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
    ax.plot([0, 1], [0, 1], color='gray', linestyle='--', linewidth=2, label='Random guess')
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    apply_plot_formatting(ax)
    ax.legend(loc='lower right', fontsize=16)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.show()

