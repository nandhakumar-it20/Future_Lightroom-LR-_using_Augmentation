import streamlit as st
import kornia
from torch import nn
import torch
from torchvision.transforms import functional as F
from torchvision.utils import make_grid
from streamlit_ace import st_ace
from PIL import Image

IS_LOCAL = False
@st.cache(suppress_st_warning=True)
def set_transform(content):
    try:
        transform = eval(content, {"kornia": kornia, "nn": nn}, None)
    except Exception as e:
        st.write(f"There was an error: {e}")
        transform = nn.Sequential()
    return transform
st.markdown("# Future_Lightroom_[LR]_using_Augmentation")
st.sidebar.markdown(
    "Enhancing using Computer Vision"
)
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    im = Image.open(uploaded_file)
else:
    im = Image.open(".jpg")
scaler = int(im.height / 2)
st.sidebar.image(im, caption="Input Image", width=256)
image = F.pil_to_tensor(im).float() / 255


predefined_transforms = [
    """
nn.Sequential(
   kornia.augmentation.RandomAffine(degrees=360,p=0.5),
   kornia.augmentation.ColorJitter(brightness=0.2, contrast=0.3, saturation=0.2, hue=0.3, p=1)
)
# p=0.5 is the probability of applying the transformation
""",
    """
nn.Sequential(
   kornia.augmentation.RandomErasing(scale=(.4, .8), ratio=(.3, 1/.3), p=0.5),
)
""",
    """
nn.Sequential(
   kornia.augmentation.RandomErasing(scale=(.4, .8), ratio=(.3, 1/.3), p=1, same_on_batch=True),
)
#By setting same_on_batch=True you can apply the same transform across the batch
""",
    f"""
nn.Sequential(
    kornia.augmentation.RandomResizedCrop(size=({scaler}, {scaler}), scale=(3., 3.), ratio=(2., 2.), p=1.),
    kornia.augmentation.RandomHorizontalFlip(p=0.7),
    kornia.augmentation.RandomGrayscale(p=0.5),
)
""",
]

selected_transform = st.selectbox(
    "Pick an augmentation pipeline example:", predefined_transforms
)

st.write("Transform to apply:")
readonly = False
content = st_ace(
    value=selected_transform,
    height=150,
    language="python",
    keybinding="vscode",
    show_gutter=True,
    show_print_margin=True,
    wrap=False,
    auto_update=False,
    readonly=readonly,
)
if content:
    transform = set_transform(content)
process = st.button("Next Batch")
image_batch = torch.stack(batch_size * [image])
image_batch.to(device)
transformeds = None
try:
    transformeds = transform(image_batch)
except Exception as e:
    st.write(f"There was an error: {e}")
cols = st.columns(4)
if transformeds is not None:
    for i, x in enumerate(transformeds):
        i = i % 4
        cols[i].image(F.to_pil_image(x), use_column_width=True)

