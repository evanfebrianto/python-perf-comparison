import subprocess
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import statistics

def run_command(command, runs=10):
    """Helper function to run a shell command multiple times and return the execution times."""
    times = []
    for _ in range(runs):
        start_time = time.time()
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        end_time = time.time()
        
        if result.returncode != 0:
            print(f"Error running command: {command}")
            print(result.stderr)
            return None
        
        times.append(end_time - start_time)
    
    return statistics.mean(times)

def measure_execution_times():
    """Measure execution times for different implementations."""
    n = 10**7
    runs = 100  # Number of runs for each implementation

    # Command to run each implementation
    commands = {
        "Normal Python": f"python sum_of_squares.py",
        "C Extension": f"python c-ext/c_ext_test.py",
        "Cython": f"python cython/cython_test.py",
        "Numba": f"python numba/numba_test.py",
        "Rust (Pure)": f"./rust_pure/target/release/rust_pure",
        "Rust (Python)": f"python rust_python/rust_python_test.py"
    }

    execution_times = {}

    for method, command in commands.items():
        print(f"Running {method}...")
        execution_time = run_command(command, runs)
        if execution_time is not None:
            execution_times[method] = execution_time
            print(f"{method} average execution time: {execution_time:.6f} seconds")

    return execution_times


def plot_execution_times(average_times):
    """Plot the average execution times using Plotly with improved design."""
    methods = list(average_times.keys())
    times = list(average_times.values())
    
    # Sort the data by execution time
    sorted_data = sorted(zip(methods, times), key=lambda x: x[1])
    methods, times = zip(*sorted_data)
    
    # Create color scale
    colors = [f'rgb({int(255 * (1 - i/len(methods)))}, {int(100 + 155 * (i/len(methods)))}, 255)' for i in range(len(methods))]
    
    # Create figure with a single plot
    fig = go.Figure()
    
    # Add bar chart
    fig.add_trace(go.Bar(
        y=methods,
        x=times,
        orientation='h',
        text=[f'{time:.4f} s' for time in times],
        textposition='outside',
        textfont=dict(size=12, color='rgba(0,0,0,0.8)'),
        marker=dict(color=colors, line=dict(width=1, color='rgba(0,0,0,0.3)')),
        hoverinfo='text',
        hovertext=[f'{method}<br>{time:.4f} s' for method, time in zip(methods, times)],
    ))
    
    # Update layout
    fig.update_layout(
        title=dict(
            text='Execution Time Comparison: Sum of Squares Implementation',
            font=dict(size=24, color='rgba(0,0,0,0.8)'),
            x=0.5,
            y=0.95,
        ),
        plot_bgcolor='rgba(240,240,240,0.5)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=600,
        margin=dict(l=0, r=0, t=100, b=0),
        xaxis=dict(
            title=dict(text='Execution Time (seconds)', font=dict(size=16)),
            showgrid=True,
            gridcolor='rgba(0,0,0,0.1)',
            zeroline=False,
        ),
        yaxis=dict(
            title=dict(text='Implementation Method', font=dict(size=16)),
            showgrid=False,
            zeroline=False,
        ),
        showlegend=False,
        annotations=[
            dict(
                text='Average of 100 Runs',
                showarrow=False,
                x=0.5,
                y=1.05,
                xref='paper',
                yref='paper',
                font=dict(size=14, color='rgba(0,0,0,0.6)'),
            )
        ],
    )
    
    # Add logo
    fig.add_layout_image(
        dict(
            source="https://python.org/static/community_logos/python-logo-master-v3-TM.png",
            xref="paper", yref="paper",
            x=1, y=1,
            sizex=0.1, sizey=0.1,
            xanchor="right", yanchor="top",
            opacity=0.8,
            layer="above"
        )
    )

    # Save the plot
    pio.write_image(fig, "execution_times_comparison.png")
    pio.write_html(fig, "execution_times_comparison.html")

def plot_performance_comparison(average_times):
    """Plot the performance comparison of methods against the baseline (Normal Python)."""
    methods = list(average_times.keys())
    times = list(average_times.values())
    
    # Find the baseline (Normal Python) execution time
    baseline_time = average_times['Normal Python']
    
    # Calculate performance improvement percentages
    performance_improvements = [(baseline_time - time) / baseline_time * 100 for time in times]
    
    # Sort the data by performance improvement
    sorted_data = sorted(zip(methods, performance_improvements), key=lambda x: x[1], reverse=True)
    methods, improvements = zip(*sorted_data)
    
    # Create color scale
    colors = [f'rgb({int(255 * (i/len(methods)))}, {int(100 + 155 * (1 - i/len(methods)))}, {int(100 + 155 * (i/len(methods)))})' for i in range(len(methods))]
    
    # Create figure
    fig = go.Figure()
    
    # Add bar chart
    fig.add_trace(go.Bar(
        y=methods,
        x=improvements,
        orientation='h',
        text=[f'{imp:.2f}%' for imp in improvements],
        textposition='outside',
        textfont=dict(size=12, color='rgba(0,0,0,0.8)'),
        marker=dict(color=colors, line=dict(width=1, color='rgba(0,0,0,0.3)')),
        hoverinfo='text',
        hovertext=[f'{method}<br>Improvement: {imp:.2f}%' for method, imp in zip(methods, improvements)],
    ))
    
    # Update layout
    fig.update_layout(
        title=dict(
            text='Performance Improvement Comparison (Relative to Normal Python)',
            font=dict(size=24, color='rgba(0,0,0,0.8)'),
            x=0.5,
            y=0.95,
        ),
        plot_bgcolor='rgba(240,240,240,0.5)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=600,
        margin=dict(l=0, r=0, t=100, b=0),
        xaxis=dict(
            title=dict(text='Performance Improvement (%)', font=dict(size=16)),
            showgrid=True,
            gridcolor='rgba(0,0,0,0.1)',
            zeroline=True,
            zerolinecolor='rgba(0,0,0,0.2)',
            zerolinewidth=2,
        ),
        yaxis=dict(
            title=dict(text='Implementation Method', font=dict(size=16)),
            showgrid=False,
            zeroline=False,
        ),
        showlegend=False,
        annotations=[
            dict(
                text='Positive values indicate faster execution than Normal Python',
                showarrow=False,
                x=0.5,
                y=1.05,
                xref='paper',
                yref='paper',
                font=dict(size=14, color='rgba(0,0,0,0.6)'),
            )
        ],
    )
    
    # Add logo
    fig.add_layout_image(
        dict(
            source="https://python.org/static/community_logos/python-logo-master-v3-TM.png",
            xref="paper", yref="paper",
            x=1, y=1,
            sizex=0.1, sizey=0.1,
            xanchor="right", yanchor="top",
            opacity=0.8,
            layer="above"
        )
    )

    # Save the plot
    pio.write_image(fig, "performance_improvement_comparison.png")
    pio.write_html(fig, "performance_improvement_comparison.html")

if __name__ == "__main__":
    average_times = measure_execution_times()
    plot_execution_times(average_times)
    plot_performance_comparison(average_times)