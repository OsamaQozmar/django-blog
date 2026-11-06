from blog.models import Post

from ..client import ContentClient
from .utils import validate_text_input

MAX_SUMMARY_LENGTH = 500
PROMPT_TARGET_LENGTH = 400


class PostNotFoundError(ValueError):
    """Raised when no post exists with the requested ID."""


def _build_summary_prompt(title, content):
    return (
        "Summarize the following blog post in clear, concise plain text. "
        f"The summary must not exceed {PROMPT_TARGET_LENGTH} characters. "
        "Return only the summary, with no preamble.\n\n"
        f"Title: {title}\n\n"
        f"Content:\n{content}"
    )


def summarize_post(post_id):
    if isinstance(post_id, bool) or not isinstance(post_id, int) or post_id <= 0:
        raise ValueError("post_id must be a positive integer.")

    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise PostNotFoundError(f"Post with id {post_id} does not exist.")

    content = validate_text_input(
        post.content, min_length=1, field_name="Post content"
    )

    summary = ContentClient().generate(_build_summary_prompt(post.title, content))
    summary = (summary or "").strip()
    if not summary:
        raise ValueError("Model output was empty or invalid.")

    if len(summary) > MAX_SUMMARY_LENGTH:
        summary = summary[: MAX_SUMMARY_LENGTH - 3].rstrip() + "..."

    return {
        "post_id": post.pk,
        "title": post.title,
        "summary": summary,
        "length": len(summary),
    }