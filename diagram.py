
import yaml 
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

### PATH ###
with open(r'C:\Users\karol\Desktop\Munka\cikkek\Images\Images\Cikk\data.yaml') as file:
    config = yaml.safe_load(file)

# Define color palette for shapes and edges
colors_shape = ["#375bff", "#fa7500", "#6cca6c", '#f0e442', '#d62722']  # Shape colors
colors_edge = ["#000000", "#be3fb8", "#727272",  "#009600", '#17becf']   # Edge colors


shapes = ["s", "D", "p", "h", "8"]
inner_shapes=[".","$|$","1","X","P","*"]
edge_shapes=[]

col = None
sha = None
texts = []
low_to_high = ['very_low', 'low', 'medium', 'high', 'very_high']
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.05,bottom=0.06,right=0.985,top=0.99)
for i in range(len(config)):
    if config['cikk_'+str(i)]['model'] == 'DH':
        sha = 0
    elif config['cikk_'+str(i)]['model'] == 'MDH':
        sha = 1
    elif config['cikk_'+str(i)]['model'] == 'MIX':
        sha = 2
    elif config['cikk_'+str(i)]['model'] == 'POE':
        sha = 3
    else:
        sha = 4
        
    if config['cikk_'+str(i)]['cost'] == 'very_low':
        col = 0
    elif config['cikk_'+str(i)]['cost'] == 'low':
        col = 1
    elif config['cikk_'+str(i)]['cost'] == 'medium':
        col = 2
    elif config['cikk_'+str(i)]['cost'] == 'high':
        col = 3
    else:
        col = 4
        
    if config['cikk_'+str(i)]['optim'] == 'LS':
        inner_sha = 0
    elif config['cikk_'+str(i)]['optim'] == 'LM':
        inner_sha = 1
    elif config['cikk_'+str(i)]['optim'] == 'BE':
        inner_sha = 2
    elif config['cikk_'+str(i)]['optim'] == 'MLE':
        inner_sha = 3
    elif config['cikk_'+str(i)]['optim'] == 'NM':
        inner_sha = 4
    else:
        inner_sha = 5
        
    if config['cikk_'+str(i)]['complex'] == 'very_low':
        complex_col = 0
    elif config['cikk_'+str(i)]['complex'] == 'low':
        complex_col = 1
    elif config['cikk_'+str(i)]['complex'] == 'medium':
        complex_col = 2
    elif config['cikk_'+str(i)]['complex'] == 'high':
        complex_col = 3
    else:
       complex_col = 4
       
    if config['cikk_'+str(i)]['compute'] == 'very_low':
        compute_col = 1
    elif config['cikk_'+str(i)]['compute'] == 'low':
        compute_col = 2
    elif config['cikk_'+str(i)]['compute'] == 'medium':
        compute_col = 3
    elif config['cikk_'+str(i)]['compute'] == 'high':
        compute_col = 4
    else:
       compute_col = 5
        
    cost_score = low_to_high.index(config['cikk_'+str(i)]['cost']) + 1
    complex_score = low_to_high.index(config['cikk_'+str(i)]['complex']) + 1
    compute_score = low_to_high.index(config['cikk_'+str(i)]['compute']) + 1
    Norm_Acc = (config['cikk_'+str(i)]['start_acc']-config['cikk_'+str(i)]['fin_acc'])/config['cikk_'+str(i)]['start_acc']
    
    CEI = Norm_Acc * 5 / (cost_score * 0.5 + complex_score * 0.35 + compute_score * 0.15)
    
    plt.scatter((config['cikk_'+str(i)]['start_acc']-config['cikk_'+str(i)]['fin_acc'])/config['cikk_'+str(i)]['start_acc'], CEI, color=colors_shape[col], s=1500, marker=shapes[sha],linewidths=5, edgecolors= colors_edge[complex_col])
    plt.scatter((config['cikk_'+str(i)]['start_acc']-config['cikk_'+str(i)]['fin_acc'])/config['cikk_'+str(i)]['start_acc'], CEI, color="k",s=500,marker=inner_shapes[inner_sha])
    
    if config['cikk_'+str(i)]["id"] == 71 or config['cikk_'+str(i)]["id"] == 22 or config['cikk_'+str(i)]["id"] == 101 or config['cikk_'+str(i)]["id"] == 81 or config['cikk_'+str(i)]["id"] == 14 or config['cikk_'+str(i)]["id"] == 73:
        ax.annotate("[" + str(config['cikk_'+str(i)]["id"]) + "](" + str(compute_col) + ")",(((config['cikk_'+str(i)]['start_acc']-config['cikk_'+str(i)]['fin_acc'])/config['cikk_'+str(i)]['start_acc'])-0.022,CEI+0.1),fontsize=20, fontweight='bold')
    elif config['cikk_'+str(i)]["id"] == 19 or config['cikk_'+str(i)]["id"] == 21:
        ax.annotate("[" + str(config['cikk_'+str(i)]["id"]) + "](" + str(compute_col) + ")",(((config['cikk_'+str(i)]['start_acc']-config['cikk_'+str(i)]['fin_acc'])/config['cikk_'+str(i)]['start_acc'])-0.022,CEI+0.1),fontsize=20, fontweight='bold')
    elif config['cikk_'+str(i)]["id"] == 94:
         ax.annotate("[" + str(config['cikk_'+str(i)]["id"]) + "](" + str(compute_col) + ")",(((config['cikk_'+str(i)]['start_acc']-config['cikk_'+str(i)]['fin_acc'])/config['cikk_'+str(i)]['start_acc'])-0.03,CEI+0.1),fontsize=20, fontweight='bold')
    elif config['cikk_'+str(i)]["id"] == 82 or config['cikk_'+str(i)]["id"] == 79 or config['cikk_'+str(i)]["id"] == 111 or config['cikk_'+str(i)]["id"] == 110 or config['cikk_'+str(i)]["id"] == 78:
         ax.annotate("[" + str(config['cikk_'+str(i)]["id"]) + "](" + str(compute_col) + ")",(((config['cikk_'+str(i)]['start_acc']-config['cikk_'+str(i)]['fin_acc'])/config['cikk_'+str(i)]['start_acc'])-0.02,CEI-0.16),fontsize=20, fontweight='bold')
    elif config['cikk_'+str(i)]["id"] == 80:
        ax.annotate("[" + str(config['cikk_'+str(i)]["id"]) + "](" + str(compute_col) + ")",(((config['cikk_'+str(i)]['start_acc']-config['cikk_'+str(i)]['fin_acc'])/config['cikk_'+str(i)]['start_acc'])-0.042,CEI-0.16),fontsize=20, fontweight='bold')
    elif config['cikk_'+str(i)]["id"] == 102:
        ax.annotate("[" + str(config['cikk_'+str(i)]["id"]) + "](" + str(compute_col) + ")",(((config['cikk_'+str(i)]['start_acc']-config['cikk_'+str(i)]['fin_acc'])/config['cikk_'+str(i)]['start_acc'])-0.009,CEI+0.1),fontsize=20, fontweight='bold')
    else:
        ax.annotate("[" + str(config['cikk_'+str(i)]["id"]) + "](" + str(compute_col) + ")" ,(((config['cikk_'+str(i)]['start_acc']-config['cikk_'+str(i)]['fin_acc'])/config['cikk_'+str(i)]['start_acc'])-0.016,CEI-0.14),fontsize=20, fontweight='bold')
    
# Function add a legend 
f = lambda m,c: plt.plot([],[],marker=m, color=c,  markersize= 25, ls="none")[0]
g = lambda m,c: plt.plot([],[],marker=m, color=c,  markersize= 40, ls="none")[0]
h = lambda m,c: plt.plot([],[],marker=m, color=c,  markersize= 24, ls="none")[0]
handles1 = [f("s", colors_shape[i]) for i in range(5)]
handles2 = [f(inner_shapes[i],"k") for i in range(6)]
handles4 = [f(shapes[i], "k") for i in range(5)]
handles5 = [f("s", colors_edge[i]) for i in range(5)]
handles3 = [g(r"$[\#]$","k")]
handles6 = [g(r"$(\#)$","k")]
handles7 = [h(r"$(1)$","k"),h(r"$(2)$","k"),h(r"$(3)$","k"),h(r"$(4)$","k"),h(r"$(5)$","k")]

model_text = ["Denavit-Hartenberg","Modified DH","Combined minimal","Product of Exponentials","Dual-quaternion"]
optim_text = ["Least-square","Levenberg-Marquart","Bayesian Estimation","Maximum Likelihood","Nelder-Mead","Genetic Algorithms",]
cost_text = ["very low (1)","low (2)","medium (3)","high (4)","very high (5)"]
cit_text = ["   Reference number"]
comput_text = ["very low","low","medium","high","very high"]

first_legend = ax.legend(handles1,cost_text,title="Estimated cost \n(shape color):",loc="best",bbox_to_anchor=(0.611,1),framealpha=1,title_fontsize=28,fontsize=28) 

second_legend = ax.legend(handles2,optim_text,title="Optimization algorithms:\n(inner shape)",loc="best",bbox_to_anchor=(0.242,0.685),framealpha=1,title_fontsize=28,fontsize=28) 

third_legend =  ax.legend(handles3,cit_text, loc="best",bbox_to_anchor=(0.468,0.684),framealpha=1,title_fontsize=6,fontsize=28) 

fifth_legend = ax.legend(handles5,cost_text,title="Setup complexity \n(edge_color):",loc="best",bbox_to_anchor=(0.447,1),framealpha=1,title_fontsize=28,fontsize=28) 

sixth_legend = ax.legend(handles7,comput_text,title="Computational \nburden (#):",bbox_to_anchor=(0.75,1),framealpha=1,title_fontsize=28,fontsize=28)

fourth_legend = plt.legend(handles4,model_text,title="Geometrical modeling method:\n(outer shape)",loc="upper left",framealpha=1,title_fontsize=28,fontsize=28) 



ax.add_artist(first_legend)
ax.add_artist(second_legend)
ax.add_artist(third_legend)
ax.add_artist(fifth_legend)
ax.add_artist(sixth_legend)

plt.xticks(fontsize=20, fontweight='bold')
plt.yticks(fontsize=20, fontweight='bold')
plt.ylabel("Calibration Efficiency Index (CEI)",fontdict={'family':'serif','size':22, 'fontweight': 'bold'})
plt.xlabel("Normalized global accuracy improvement",fontdict={'family':'serif','size':22, 'fontweight': 'bold'})
ax.set_xlim([0.1, 1])
ax.set_ylim([0, 3.3])
plt.show()

