import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self, image_size):
        super(Net, self).__init__()
        self.image_size = image_size

        # ...

    def forward(self, x):
        # ...

        # Resize the input tensor before the view operation
        x = F.interpolate(x, size=(self.image_size // 4, self.image_size // 4), mode='bilinear', align_corners=False)

        # Flatten the output for the fully connected layers
        x = x.view(x.size(0), -1)

        # ...

        return clsf, x1.squeeze(), y1.squeeze(), x2.squeeze(), y2.squeeze()