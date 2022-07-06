using MayaTaskManager;

namespace BackServer;

public class Worker : BackgroundService
{
    private readonly ILogger<Worker> _logger;

    public Worker(ILogger<Worker> logger)
    {
        _logger = logger;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            _logger.LogInformation("QN后台服务开始: {time}", DateTimeOffset.Now);
            TaskServer a = new TaskServer("127.0.0.1", 10340,_logger);
            await a.Start();
            await Task.Delay(1000, stoppingToken);
        }
    }
    public override Task StopAsync(CancellationToken cancellationToken)
    {
        _logger.LogInformation("QN后台服务停止: {time}", DateTimeOffset.Now);
        return base.StopAsync(cancellationToken);
    }
}
