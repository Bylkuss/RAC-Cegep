using Avalonia.Controls;
using Avalonia.Markup.Xaml;
using StreamingApp.ViewModels;

namespace StreamingApp.Views;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
        DataContext = new MainViewModel();
    }
    private void InitializeComponent()
    {
        AvaloniaXamlLoader.Load(this);
    }
}