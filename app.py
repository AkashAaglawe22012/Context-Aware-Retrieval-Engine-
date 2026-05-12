import numpy as np
from sentence_transformers import SentenceTransformer
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import faiss


class RAG:

    def __init__(self, text):
        self.text = text

    def create_embedding(self, chunk_texts, query, ex_q):
        model = SentenceTransformer("all-MiniLM-L6-v2")
        embeddings = model.encode(chunk_texts)

        embeddings = np.array(embeddings).astype("float32")
        dimension = embeddings.shape[1]

        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings)


        query_embedding = model.encode([query])
        query_embedding = np.array(query_embedding).astype("float32")
        distances, indices = index.search(query_embedding, 3)
        resuklt_A = []
        for idx in indices[0]:
            print(chunk_texts[idx])
            resuklt_A.append(chunk_texts[idx])

        query_embedding_2 = model.encode([ex_q])
        query_embedding_2 = np.array(query_embedding_2).astype("float32")
        distances, indices_2 = index.search(query_embedding_2, 3)
        resuklt_B = []
        for idx in indices_2[0]:
            print(chunk_texts[idx])
            resuklt_B.append(chunk_texts[idx])

        return resuklt_A, resuklt_B

    def expand_query(self, query):
        query_lower = query.lower().strip()
        # LLMs

        if "llm" in query_lower or "large language model" in query_lower:

            return (
                "Explain how large language models are trained on massive "
                "text datasets to perform reasoning, text generation, "
                "code generation, summarization, and contextual language "
                "understanding across enterprise AI applications."
            )

        # Transformer Architecture
        elif "transformer" in query_lower or "self-attention" in query_lower:

            return (
                "Describe how transformer architecture uses self-attention "
                "mechanisms, parallel computation, and contextual dependency "
                "modeling to improve reasoning and long-text understanding "
                "in modern large language models."
            )

        # Tokens
        elif "token" in query_lower or "tokenization" in query_lower:

            return (
                "Explain how tokenization converts text into smaller processing "
                "units used during training and inference, and how token count "
                "affects memory usage, latency, inference cost, and context "
                "window limitations in enterprise AI systems."
            )

        # Temperature
        elif "temperature" in query_lower:

            return (
                "Describe how temperature settings control randomness, "
                "creativity, determinism, and hallucination probability "
                "during large language model inference and response generation."
            )

        # Top-k / Top-p
        elif (
            "top-k" in query_lower
            or "top p" in query_lower
            or "top-p" in query_lower
            or "sampling" in query_lower
        ):

            return (
                "Explain how top-k sampling and top-p sampling improve "
                "response generation quality by restricting token selection "
                "based on probability distributions during language model decoding."
            )

        # Prompt Engineering
        elif "prompt" in query_lower or "prompt engineering" in query_lower:

            return (
                "Describe how prompt engineering techniques such as "
                "chain-of-thought prompting, role prompting, instruction "
                "formatting, and few-shot learning improve reasoning quality "
                "and reliability in large language model applications."
            )

        # AI Agents
        elif "agent" in query_lower and "multi-agent" not in query_lower:

            return (
                "Explain how autonomous AI agents perform reasoning, "
                "planning, memory management, tool execution, and iterative "
                "decision-making to automate complex enterprise workflows "
                "using large language models."
            )

        # Frameworks
        elif (
            "langchain" in query_lower
            or "langgraph" in query_lower
            or "autogen" in query_lower
            or "crewai" in query_lower
            or "semantic kernel" in query_lower
            or "framework" in query_lower
        ):

            return (
                "Describe how agentic AI frameworks such as LangChain, "
                "LangGraph, AutoGen, CrewAI, and Semantic Kernel provide "
                "workflow orchestration, memory management, tool calling, "
                "state handling, and multi-agent collaboration capabilities."
            )

        # Multi-Agent Systems
        elif "multi-agent" in query_lower or "multiple agents" in query_lower:

            return (
                "Explain how multi-agent AI systems distribute responsibilities "
                "across specialized agents responsible for planning, retrieval, "
                "reasoning, validation, summarization, and response generation "
                "within enterprise automation platforms."
            )

        # RAG
        elif "rag" in query_lower or "retrieval augmented generation" in query_lower:

            return (
                "Describe how Retrieval-Augmented Generation combines large "
                "language models with semantic retrieval systems, vector "
                "databases, embeddings, and external knowledge sources to "
                "generate grounded and factually accurate responses."
            )

        # RAG Pipeline
        elif "rag pipeline" in query_lower or "retrieval pipeline" in query_lower:

            return (
                "Explain the stages of a Retrieval-Augmented Generation pipeline "
                "including ingestion, chunking, embedding generation, vector "
                "indexing, semantic retrieval, reranking, and response synthesis."
            )

        # Embeddings
        elif "embedding" in query_lower:

            return (
                "Describe how embedding models convert text into high-dimensional "
                "semantic vector representations used for similarity search, "
                "clustering, recommendation systems, and retrieval operations "
                "within RAG architectures."
            )

        # Vector Databases
        elif (
            "vector database" in query_lower
            or "faiss" in query_lower
            or "pinecone" in query_lower
            or "weaviate" in query_lower
            or "milvus" in query_lower
            or "chromadb" in query_lower
        ):

            return (
                "Explain how vector databases store embedding vectors and "
                "perform semantic similarity search using Approximate Nearest "
                "Neighbor algorithms such as HNSW and IVF in scalable AI systems."
            )

        # Agentic RAG
        elif "agentic rag" in query_lower or (
            "agent" in query_lower and "rag" in query_lower
        ):

            return (
                "Describe how agentic RAG systems combine autonomous AI agents "
                "with retrieval pipelines to support reasoning, planning, "
                "validation, memory management, tool usage, and adaptive "
                "knowledge retrieval in enterprise AI applications."
            )

        # MCP
        elif "mcp" in query_lower or "model context protocol" in query_lower:

            return (
                "Explain how Model Context Protocol enables AI agents and "
                "language models to interact with APIs, databases, browsers, "
                "cloud systems, and enterprise tools through standardized "
                "communication interfaces."
            )

        # MCP Servers
        elif "mcp server" in query_lower:

            return (
                "Describe how MCP servers centralize tool integration, "
                "authentication, authorization, logging, and reusable API "
                "execution capabilities for scalable enterprise AI systems."
            )

        # Memory
        elif "memory" in query_lower:

            return (
                "Explain how short-term memory, long-term memory, episodic "
                "memory, and semantic memory maintain contextual continuity, "
                "historical knowledge, and reasoning consistency in advanced "
                "agentic AI systems."
            )

        # Observability
        elif "observability" in query_lower or "monitoring" in query_lower:

            return (
                "Describe how observability platforms monitor token usage, "
                "latency, hallucination rates, retrieval quality, workflow "
                "execution, and agent behavior in production-grade AI systems."
            )

        # Security
        elif (
            "security" in query_lower
            or "prompt injection" in query_lower
            or "guardrails" in query_lower
        ):

            return (
                "Explain the major security challenges in enterprise AI systems "
                "including prompt injection attacks, unsafe tool execution, "
                "retrieval poisoning, authentication, access control, "
                "sandboxing, and AI governance mechanisms."
            )

        # Future of AI
        elif (
            "future" in query_lower
            or "future of ai" in query_lower
            or "future of artificial intelligence" in query_lower
        ):

            return (
                "Describe how the future of artificial intelligence is evolving "
                "toward autonomous multi-agent ecosystems capable of reasoning, "
                "memory management, multimodal retrieval, reinforcement learning, "
                "real-time tool execution, and enterprise-scale autonomous automation."
            )

        # Multimodal AI
        elif "multimodal" in query_lower or "text audio video image" in query_lower:

            return (
                "Explain how multimodal AI systems combine text, audio, images, "
                "and video understanding with retrieval, reasoning, and "
                "generation capabilities in next-generation enterprise AI platforms."
            )

        # Default
        return query_lower

    def splitter(self, query):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)

        chunk_texts = text_splitter.split_text(self.text)
        ex_q = self.expand_query(query)
        return self.create_embedding(chunk_texts, query, ex_q)


# with open("document.txt", "r", encoding="utf-8") as file:
#     text = file.read()
# query = "what is Multimodal AI?"
# r = RAG(text)
# a, b = r.splitter(query)

# print("A === ", a)
# print("B === ", b)
