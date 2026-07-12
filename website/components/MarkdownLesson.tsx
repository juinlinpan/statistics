import ReactMarkdown from "react-markdown";
import rehypeKatex from "rehype-katex";
import rehypeRaw from "rehype-raw";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";

export function MarkdownLesson({ content }: { content: string }) {
  return (
    <article className="lesson-prose">
      <ReactMarkdown remarkPlugins={[remarkGfm, remarkMath]} rehypePlugins={[rehypeRaw, rehypeKatex]}>
        {content}
      </ReactMarkdown>
    </article>
  );
}
